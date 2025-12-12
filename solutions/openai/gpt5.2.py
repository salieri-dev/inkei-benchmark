from __future__ import annotations

from dataclasses import dataclass
import html as _html
import math
import re
from typing import List, Optional, Tuple

from PIL import Image, ImageDraw


# ----------------------------
# Data structures
# ----------------------------

@dataclass(frozen=True)
class Path2D:
    x: List[float]
    y: List[float]


@dataclass(frozen=True)
class Path3D:
    x: List[float]
    y: List[float]
    z: List[float]


@dataclass
class LayerParams:
    # p0..p9 (same naming as the JS)
    p0: float
    p1: float
    p2: float
    p3: float
    p4: float
    p5: float
    p6: float
    p7: float
    p8: float
    p9: float

    # drawing params
    lp: float = 100.0  # line alpha percent
    fp: float = 20.0   # fill alpha percent (not used here)
    lw: float = 2.0    # line width
    as_: float = 8.0   # animation seconds (not used here)

    lc: str = "FFFFFF"
    fc: str = "FFFFFF"

    # label strings
    q0: str = "-"
    q1: str = "-"
    q2: str = "-"


# ----------------------------
# Helpers
# ----------------------------

_NUM_RE = re.compile(r"^[+-]?\d+(?:\.\d+)?$")


def _parse_number(s: str, default: float) -> float:
    s = s.strip()
    if not s:
        return default
    if _NUM_RE.match(s):
        try:
            v = float(s)
            if v.is_integer():
                return float(int(v))
            return v
        except ValueError:
            return default
    return default


def _hex_to_rgba(hex6: str, alpha_01: float) -> Tuple[int, int, int, int]:
    h = (hex6 or "").strip().lstrip("#")
    if len(h) != 6 or any(c not in "0123456789abcdefABCDEF" for c in h):
        h = "000000"
    r = int(h[0:2], 16)
    g = int(h[2:4], 16)
    b = int(h[4:6], 16)
    a = int(max(0.0, min(1.0, alpha_01)) * 255)
    return r, g, b, a


def _sample_cubic_bezier(
    p0: Tuple[float, float],
    p1: Tuple[float, float],
    p2: Tuple[float, float],
    p3: Tuple[float, float],
    steps: int = 30,
) -> List[Tuple[float, float]]:
    pts: List[Tuple[float, float]] = []
    for i in range(steps + 1):
        t = i / steps
        mt = 1.0 - t
        x = (
            (mt * mt * mt) * p0[0]
            + 3 * t * (mt * mt) * p1[0]
            + 3 * (t * t) * mt * p2[0]
            + (t * t * t) * p3[0]
        )
        y = (
            (mt * mt * mt) * p0[1]
            + 3 * t * (mt * mt) * p1[1]
            + 3 * (t * t) * mt * p2[1]
            + (t * t * t) * p3[1]
        )
        pts.append((x, y))
    return pts


# ----------------------------
# Port of clsMorph (subset)
# ----------------------------

class Morph:
    @staticmethod
    def rotate2d(base_x: float, base_y: float, x: float, y: float, angle_deg: float) -> Tuple[float, float]:
        if angle_deg % 360 == 0:
            return x, y
        r = math.hypot(x - base_x, y - base_y)
        ang = math.degrees(math.atan2(y - base_y, x - base_x)) + angle_deg
        rad = math.radians(ang)
        return base_x + math.cos(rad) * r, base_y + math.sin(rad) * r

    @staticmethod
    def _minmax(arr: List[float]) -> Tuple[float, float]:
        mn = None
        mx = None
        for v in arr:
            if mn is None or v < mn:
                mn = v
            if mx is None or v > mx:
                mx = v
        if mn is None or mx is None:
            return 0.0, 0.0
        return mn, mx

    @staticmethod
    def center_array(arr: List[float]) -> float:
        mn, mx = Morph._minmax(arr)
        return mn + 0.5 * (mx - mn)

    @staticmethod
    def center_path3d(path: Path3D) -> Tuple[float, float, float]:
        return (
            Morph.center_array(path.x),
            Morph.center_array(path.y),
            Morph.center_array(path.z),
        )

    @staticmethod
    def get_perspective_size3d(panel_w: float, path: Path3D, stage_w: float) -> float:
        # Port of clsMorph.fnGetPerspectiveSize3d
        min_x = max_x = min_y = max_y = min_z = max_z = None

        for i in range(len(path.x)):
            px = path.x[i] * panel_w / stage_w
            py = path.y[i] * panel_w / stage_w
            pz = path.z[i] * panel_w / stage_w

            min_x = px if min_x is None else min(min_x, px)
            max_x = px if max_x is None else max(max_x, px)
            min_y = py if min_y is None else min(min_y, py)
            max_y = py if max_y is None else max(max_y, py)
            min_z = pz if min_z is None else min(min_z, pz)
            max_z = pz if max_z is None else max(max_z, pz)

        w = int(math.floor((max_x - min_x))) if min_x is not None else 0
        h = int(math.floor((max_y - min_y))) if min_y is not None else 0
        d = int(math.floor((max_z - min_z))) if min_z is not None else 0
        e = max(w, h, d)
        return float(e if e > 1 else 1)

    @staticmethod
    def morph_path3d(a: Path3D, b: Path3D, per: float) -> Path3D:
        # Port of clsMorph.fnGetMophPath3d
        if (
            len(a.x) != len(b.x)
            or len(a.y) != len(b.y)
            or len(a.z) != len(b.z)
            or per == 0
        ):
            return Path3D(list(a.x), list(a.y), list(a.z))
        if per == 1:
            return Path3D(list(b.x), list(b.y), list(b.z))

        x = [a.x[i] + (b.x[i] - a.x[i]) * per for i in range(len(a.x))]
        y = [a.y[i] + (b.y[i] - a.y[i]) * per for i in range(len(a.y))]
        z = [a.z[i] + (b.z[i] - a.z[i]) * per for i in range(len(a.z))]
        return Path3D(x, y, z)

    @staticmethod
    def conv_xy_to_xyz_of_cylinder3d(
        shape: Path2D,
        start_idx: List[int],
        end_idx: List[int],
        slices: int,
        slice_mask: List[int],
        segment_mask: List[int],
        radius_scale: Optional[List[float]] = None,
    ) -> Path3D:
        # Port of clsMorph.fnConvXYtoXYZofCylinder3d (in common_0.js)
        if radius_scale is None:
            radius_scale = [1.0]
        scale_len = len(radius_scale)

        left_x: List[float] = []
        left_y: List[float] = []
        right_x: List[float] = []
        right_y: List[float] = []

        # Build paired profile points
        if len(start_idx) == 1:
            st = start_idx[0]
            ed = end_idx[0]
            r = int(math.floor((ed - st) / 2))
            for t in range(0, r, 3):
                for i2 in range(4):
                    idx_l = st + (t + i2)
                    idx_r = ed - (t + i2)
                    left_x.append(shape.x[idx_l])
                    left_y.append(shape.y[idx_l])
                    right_x.append(shape.x[idx_r])
                    right_y.append(shape.y[idx_r])
        else:
            for i in range(len(end_idx)):
                left_x.append(shape.x[start_idx[i]])
                left_y.append(shape.y[start_idx[i]])
                right_x.append(shape.x[end_idx[i]])
                right_y.append(shape.y[end_idx[i]])

        m = len(left_x)  # points per slice

        # Revolve around axis
        base_x: List[float] = []
        base_y: List[float] = []
        base_z: List[float] = []
        visible: List[bool] = []

        step_deg = 360.0 / slices

        for slice_i in range(slices):
            angle_deg = 270.0 + slice_i * step_deg
            ang = math.radians(angle_deg)
            is_slice_visible = True
            if slice_i < len(slice_mask):
                is_slice_visible = (slice_mask[slice_i] == 1)

            s = math.sin(ang)
            c = math.cos(ang)

            for t in range(m):
                vx = 0.5 * (right_x[t] - left_x[t])
                cy = left_y[t] + 0.5 * (right_y[t] - left_y[t])
                vy = 0.5 * (right_y[t] - left_y[t])
                rad = math.sqrt(vx * vx + vy * vy)

                # Choose radius scaling bucket like JS:
                # v = floor((t+2)/4)
                bucket = int(math.floor((t + 2) / 4.0))
                if scale_len == 1:
                    sc = radius_scale[0]
                else:
                    sc = radius_scale[bucket] if bucket < scale_len else 1.0

                x = left_x[t] + 0.5 * (right_x[t] - left_x[t]) + s * vx
                y = cy + s * vy
                z = c * rad * sc

                base_x.append(x)
                base_y.append(y)
                base_z.append(z)
                visible.append(is_slice_visible)

        # Add connecting "quad" segments as cubic-bezier straight lines (P,P,Q,Q)
        # JS loops t=0..m step 4 (inclusive), but relies on JS returning undefined
        # for out-of-range reads. In Python we only generate segments that will be visible.
        for seg_i, t in enumerate(range(0, m + 1, 4)):
            # A = g < f.length ? (1==f[g]) : (t<m)
            if seg_i < len(segment_mask):
                A = (segment_mask[seg_i] == 1)
            else:
                A = (t < m)
            if not A:
                continue
            if t >= m:
                continue

            for slice_i in range(slices):
                k_ok = True
                h_ok = True
                if slice_i < len(slice_mask):
                    k_ok = (slice_mask[slice_i] == 1)
                if (slice_i + 1) < len(slice_mask):
                    h_ok = (slice_mask[slice_i + 1] == 1)

                if not (k_ok and h_ok):
                    continue

                n = slice_i * m + t
                p = ((slice_i + 1) % slices) * m + t

                # Straight line as cubic bezier: (P,P,Q,Q)
                for _ in range(2):
                    base_x.append(base_x[n])
                    base_y.append(base_y[n])
                    base_z.append(base_z[n])
                    visible.append(True)
                for _ in range(2):
                    base_x.append(base_x[p])
                    base_y.append(base_y[p])
                    base_z.append(base_z[p])
                    visible.append(True)

        # Swap X<->Z like JS
        base_x, base_z = base_z, base_x

        # Filter by visible
        out_x: List[float] = []
        out_y: List[float] = []
        out_z: List[float] = []
        for i, ok in enumerate(visible):
            if ok:
                out_x.append(base_x[i])
                out_y.append(base_y[i])
                out_z.append(base_z[i])

        return Path3D(out_x, out_y, out_z)

    @staticmethod
    def project_xy3d_only(
        scale_a: float,
        path: Path3D,
        stage_w: float,
        perspective_d: float,
        origin_x: float,
        origin_y: float,
        center_x: float,
        center_y: float,
        center_z: float,
        angle_x: float,
        angle_y: float,
        angle_z: float,
        morph_per: float,
        mode: str = "l",
    ) -> Path2D:
        # Port of clsMorph.fnGetXY3dOnly
        group = 4 if mode == "c" else 2

        t: List[float] = []
        q: List[float] = []
        u: List[float] = []

        for i in range(len(path.x)):
            t.append((path.x[i] - center_x) * scale_a / stage_w)
            q.append((path.y[i] - center_y) * scale_a / stage_w)
            u.append((path.z[i] - center_z) * scale_a / stage_w)

        # Morph-compress within each segment group like the JS
        if morph_per < 0:
            k = -morph_per
            for i in range(len(t)):
                end_idx = (i // group) * group + (group - 1)
                if i != end_idx and end_idx < len(t):
                    t[i] = t[end_idx] + (t[i] - t[end_idx]) * k
                    q[i] = q[end_idx] + (q[i] - q[end_idx]) * k
                    u[i] = u[end_idx] + (u[i] - u[end_idx]) * k
        elif morph_per < 1:
            k = morph_per
            for i in range(len(t)):
                start_idx = (i // group) * group
                if i != start_idx:
                    t[i] = t[start_idx] + (t[i] - t[start_idx]) * k
                    q[i] = q[start_idx] + (q[i] - q[start_idx]) * k
                    u[i] = u[start_idx] + (u[i] - u[start_idx]) * k

        # Rotate in 3 planes (same order as JS)
        for i in range(len(t)):
            if angle_z % 360 != 0:
                t[i], q[i] = Morph.rotate2d(0, 0, t[i], q[i], angle_z)
            if angle_x % 360 != 0:
                q[i], u[i] = Morph.rotate2d(0, 0, q[i], u[i], angle_x)
            if angle_y % 360 != 0:
                u[i], t[i] = Morph.rotate2d(0, 0, u[i], t[i], -angle_y)

        # Perspective + translate to screen
        for i in range(len(t)):
            per = (-u[i] + perspective_d) / perspective_d
            t[i] = origin_x + t[i] * per
            q[i] = origin_y + q[i] * per

        return Path2D(t, q)


# ----------------------------
# Port of clsShapeInkei (subset)
# ----------------------------

class ShapeInkei:
    # constants from orig_inkei.js
    iMainSt = 0
    iMainEd = 24

    iDefAx = -150
    iDefAy = 0
    iDefAa = 0

    iDefP0 = 140
    iDefP1 = 140
    iDefP2 = 10
    iDefP3 = 10
    iDefP4 = 0
    iDefP5 = 100
    iDefP6 = 100
    iDefP7 = 0
    iDefP8 = 0
    iDefP9 = 0

    I_KUKI0 = 0
    I_KUKI1 = 3
    I_KITO0 = 6
    I_KITO1 = 9
    I_RINKO = 12
    I_KITO2 = 15
    I_KITO3 = 18
    I_KUKI2 = 21
    I_KUKI3 = 24

    iStageWidth = 320
    aiAutoX = [0, 0, 0, 90, 0]
    aiAutoY = [-160, -90, 180, 360, 630]
    aiAutoZ = [0, 0, 0, 0, 0]

    @staticmethod
    def get_fny0(iP0, iP1, iP2, iP3, iP4, iP5, iP6, iP7, iP8, iP9) -> Path2D:
        return ShapeInkei.get_path(90, 80, -20, -40, -30, 140, 80, iP7, iP8, iP9)

    @staticmethod
    def get_path(iAl, iRf, iSv, iSa, iHa, iSe, iHe, iP7, iP8, iP9) -> Path2D:
        # Base control points (3*n+1 = 25)
        aiX = [0, 29, 55, 84, 86, 89, 91, 92, 93, 96, 105, 124, 129, 128, 123, 116, 113, 113, 111, 109, 106, 103, 66, 34, 0]
        aiY = [0, 2, 3, 1, 2, 2, 4, 2, 0, -3, 0, 1, 13, 21, 29, 32, 31, 31, 30, 31, 32, 33, 36, 35, 35]

        KUKI0 = ShapeInkei.I_KUKI0
        KUKI1 = ShapeInkei.I_KUKI1
        KITO0 = ShapeInkei.I_KITO0
        KITO1 = ShapeInkei.I_KITO1
        RINKO = ShapeInkei.I_RINKO
        KITO2 = ShapeInkei.I_KITO2
        KITO3 = ShapeInkei.I_KITO3
        KUKI2 = ShapeInkei.I_KUKI2
        KUKI3 = ShapeInkei.I_KUKI3

        # circumference -> diameter
        chokei = iRf / math.pi

        # vertical scale factor
        pr = chokei / (aiY[KUKI3] - aiY[KUKI0])
        for i in range(len(aiX)):
            aiY[i] = aiY[i] * pr

        # adjust glans width factor if it would invert
        if aiX[RINKO] + (aiX[KUKI1] - aiX[RINKO]) * pr < aiX[KUKI0] + (aiX[RINKO] - aiX[KUKI0]) * 0.1:
            pr = (aiX[KUKI0] + (aiX[RINKO] - aiX[KUKI0]) * 1.0) / (aiX[RINKO] - aiX[KUKI1])

        # apply to glans-side x
        for i in range(KUKI1, KUKI2 + 1):
            aiX[i] = aiX[RINKO] + (aiX[i] - aiX[RINKO]) * pr

        # glans expansion (iHe)
        cx = aiX[KITO0] + (aiX[KITO3] - aiX[KITO0]) * 0.5
        cy = aiY[KITO0] + (aiY[KITO3] - aiY[KITO0]) * 0.5
        he = iHe / 100.0
        for i in range(KITO1 - 1, KITO2 + 2):
            aiX[i] = cx + (aiX[i] - cx) * he
            aiY[i] = cy + (aiY[i] - cy) * he

        # shaft expansion (iSe)
        cx = aiX[KUKI0] + (aiX[KUKI2] - aiX[KUKI0]) * 0.5
        cy = aiY[KUKI0] + (aiY[KUKI2] - aiY[KUKI0]) * 0.5
        se = iSe / 100.0
        for i in range(KUKI0 + 1, KUKI3):
            if i <= KUKI1 - 1 or i >= KUKI2 + 1:
                aiX[i] = cx + (aiX[i] - cx) * se
                aiY[i] = cy + (aiY[i] - cy) * se

        # horizontal scale to match length iAl
        pr = iAl / (aiX[RINKO] - aiX[KUKI0])
        tip_x = aiX[RINKO] * pr
        dx = tip_x - aiX[RINKO]

        # move glans block by dx
        for i in range(KUKI1, KUKI2 + 1):
            aiX[i] += dx

        # fix shaft control points
        for i in range(1, 3):
            aiX[KUKI0 + i] = aiX[KUKI0] + (aiX[KUKI1] - aiX[KUKI0]) * i / 3.0
            aiX[KUKI3 - i] = aiX[KUKI3] + (aiX[KUKI2] - aiX[KUKI3]) * i / 3.0

        # shaft curve iSv
        cx = aiX[KUKI0 + 1] + (aiX[KUKI0 + 2] - aiX[KUKI0 + 1]) * 0.5
        cy = aiY[KUKI0 + 1] + (aiY[KUKI0 + 2] - aiY[KUKI0 + 1]) * 0.5

        r = math.hypot(cx, cy)
        s = math.degrees(math.atan2(cy, cx))
        s -= iSv
        dy = cy - (math.sin(math.radians(s)) * r)

        for i in range(KUKI0 + 1, KUKI3):
            if i <= KUKI1 - 1 or i >= KUKI2 + 1:
                aiY[i] += dy

        sv_sted = 1.0 / math.cos(math.radians(iSv))
        sv_sted = (sv_sted - 1.0) * 0.5 + 1.0
        aiY[KUKI0] *= sv_sted
        aiY[KUKI3] *= sv_sted

        # rotate boundary area by -iSv
        cx = aiX[KUKI1] + (aiX[KUKI2] - aiX[KUKI1]) * 0.5
        cy = aiY[KUKI1] + (aiY[KUKI2] - aiY[KUKI1]) * 0.5
        for i in range(KUKI1, KUKI2 + 1):
            aiX[i], aiY[i] = Morph.rotate2d(cx, cy, aiX[i], aiY[i], -iSv)

        # shaft angle iSa around base point
        bx = aiX[KUKI0]
        by = aiY[KUKI0]
        for i in range(KUKI0 + 1, KUKI3):
            aiX[i], aiY[i] = Morph.rotate2d(bx, by, aiX[i], aiY[i], -iSa)

        sa_sted = 1.0 / math.cos(math.radians(iSa))
        aiY[KUKI0] *= sa_sted
        aiY[KUKI3] *= sa_sted

        # glans angle iHa around glans center
        cx = aiX[KITO1] + (aiX[KITO2] - aiX[KITO1]) * 0.5
        cy = aiY[KITO1] + (aiY[KITO2] - aiY[KITO1]) * 0.5
        for i in range(RINKO - 1, RINKO + 2):
            aiX[i], aiY[i] = Morph.rotate2d(cx, cy, aiX[i], aiY[i], -iHa)

        # vertical centering
        height = aiY[KUKI3] - aiY[KUKI0]
        for i in range(len(aiX)):
            aiY[i] -= height * 0.5

        return Path2D([float(v) for v in aiX], [float(v) for v in aiY])

    @staticmethod
    def conv3d(shape2d: Path2D) -> Path3D:
        return Morph.conv_xy_to_xyz_of_cylinder3d(
            shape=shape2d,
            start_idx=[ShapeInkei.iMainSt],
            end_idx=[ShapeInkei.iMainEd],
            slices=12,
            slice_mask=[],
            segment_mask=[0, 0],
            radius_scale=[1.0],
        )

    @staticmethod
    def get_path3d(iP0, iP1, iP2, iP3, iP4, iP5, iP6, iP7, iP8, iP9, mode: str = "") -> Path3D:
        if mode == "click":
            s2d = ShapeInkei.get_fny0(iP0, iP1, iP2, iP3, iP4, iP5, iP6, iP7, iP8, iP9)
        else:
            s2d = ShapeInkei.get_path(iP0, iP1, iP2, iP3, iP4, iP5, iP6, iP7, iP8, iP9)
        return ShapeInkei.conv3d(s2d)

    @staticmethod
    def get_desc_list(lang: str, p: LayerParams) -> str:
        # Port of clsShapeInkei.fnGetDescList
        dia = int(math.floor(p.p1 / math.pi))
        return (
            f"Length : {int(p.p0)}mm\n"
            f"Diameter : \u03c6{dia}mm\n"
            f"Shaft Curve : {int(p.p2)}\u00b0\n"
            f"Shaft Angle : {int(p.p3)}\u00b0\n"
            f"Glans Angle : {int(p.p4)}\u00b0\n"
            f"Shaft Expansion rate : {int(p.p5)}%\n"
            f"Glans Expansion rate : {int(p.p6)}%\n"
        )


# ----------------------------
# Port of the txtCsv parsing logic (from main_u3d.js)
# ----------------------------

def _prefix_len_from_seed(seed: str = "inkei.net") -> int:
    chars = list(seed)
    w = -20
    for ch in chars[max(0, len(chars) - 9):]:
        w += ord(ch)
    return (w % 60) + (w % 76) - 84


def parse_txtcsv_layers(txtcsv: str, seed: str = "inkei.net") -> List[LayerParams]:
    pref_len = _prefix_len_from_seed(seed)
    if pref_len <= 0:
        pref_len = 2  # safe fallback

    layers: List[LayerParams] = []
    raw_layers = (txtcsv or "").split("!")

    for layer_idx, raw in enumerate(raw_layers):
        # defaults (same as main_u3d.js)
        p0 = float(ShapeInkei.iDefP0)
        p1 = float(ShapeInkei.iDefP1)
        p2 = float(ShapeInkei.iDefP2)
        p3 = float(ShapeInkei.iDefP3)
        p4 = float(ShapeInkei.iDefP4)
        p5 = float(ShapeInkei.iDefP5)
        p6 = float(ShapeInkei.iDefP6)
        p7 = float(ShapeInkei.iDefP7)
        p8 = float(ShapeInkei.iDefP8)
        p9 = float(ShapeInkei.iDefP9)

        lp = 100.0
        fp = 20.0
        lw = 2.0
        as_ = 8.0

        lc = "FFFFFF"
        fc = lc  # original JS doesn’t actually apply fc separately

        q0 = q1 = q2 = "-"

        found_any = False

        raw = re.sub(r"~+", "~", raw or "")
        for token in raw.split("~"):
            if not token:
                continue
            key = token[:pref_len]
            val = token[pref_len:]

            if key == "p0":
                p0 = _parse_number(val, p0); found_any = True
            elif key == "p1":
                p1 = _parse_number(val, p1); found_any = True
            elif key == "p2":
                p2 = _parse_number(val, p2); found_any = True
            elif key == "p3":
                p3 = _parse_number(val, p3); found_any = True
            elif key == "p4":
                p4 = _parse_number(val, p4); found_any = True
            elif key == "p5":
                p5 = _parse_number(val, p5); found_any = True
            elif key == "p6":
                p6 = _parse_number(val, p6); found_any = True
            elif key == "p7":
                p7 = _parse_number(val, p7); found_any = True
            elif key == "p8":
                p8 = _parse_number(val, p8); found_any = True
            elif key == "p9":
                p9 = _parse_number(val, p9); found_any = True
            elif key == "lp":
                lp = _parse_number(val, lp); found_any = True
            elif key == "fp":
                fp = _parse_number(val, fp); found_any = True
            elif key == "lw":
                lw = _parse_number(val, lw); found_any = True
            elif key == "as":
                as_ = _parse_number(val, as_); found_any = True
            elif key == "lc":
                lc = (val or lc).strip().lstrip("#"); found_any = True
                fc = lc
            elif key == "fc":
                # kept for completeness
                fc = (val or fc).strip().lstrip("#"); found_any = True
            elif key == "q0":
                q0 = _html.unescape(val); found_any = True
            elif key == "q1":
                q1 = _html.unescape(val); found_any = True
            elif key == "q2":
                q2 = _html.unescape(val); found_any = True

        # JS keeps layer 0 even if "found_any" is false
        if layer_idx == 0 or found_any:
            layers.append(
                LayerParams(
                    p0=p0, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9,
                    lp=lp, fp=fp, lw=lw, as_=as_,
                    lc=lc, fc=fc,
                    q0=q0, q1=q1, q2=q2,
                )
            )

    return layers


# ----------------------------
# Simple renderer (Python replacement for canvas drawing)
# ----------------------------

def render_png_from_txtcsv(
    txtcsv: str,
    out_path: str,
    size: int = 640,
    background_hex: str = "111111",
    grid_hex: str = "444444",
    angles_deg: Tuple[float, float, float] = (0.0, -160.0, 0.0),  # (X,Y,Z) like the site default view
) -> None:
    layers = parse_txtcsv_layers(txtcsv)

    # Build 3D paths
    built = []
    for lp in layers:
        p3d = ShapeInkei.get_path3d(lp.p0, lp.p1, lp.p2, lp.p3, lp.p4, lp.p5, lp.p6, lp.p7, lp.p8, lp.p9)
        cx, cy, cz = Morph.center_path3d(p3d)
        built.append((lp, p3d, (cx, cy, cz)))

    stage_w = float(ShapeInkei.iStageWidth)

    # Perspective like the JS does: iPerspective = 2 * max(get_perspective_size3d(...))
    persp_size = 1.0
    for _, p3d, _ in built:
        persp_size = max(persp_size, Morph.get_perspective_size3d(size, p3d, stage_w))
    perspective_d = 2.0 * persp_size

    img = Image.new("RGBA", (size, size), _hex_to_rgba(background_hex, 1.0))
    draw = ImageDraw.Draw(img, "RGBA")

    # Grid (matches clsAnime.sbDrawStage logic closely)
    if background_hex.strip().lstrip("#").lower() != grid_hex.strip().lstrip("#").lower():
        step = int(size / (ShapeInkei.iStageWidth / 10))  # 640/(320/10)=20
        col = _hex_to_rgba(grid_hex, 1.0)
        for x in range(0, size + 1, step):
            draw.line([(x, 0), (x, size)], fill=col, width=1)
            draw.line([(0, x), (size, x)], fill=col, width=1)

    # Project + draw cubic bezier segments
    scale_a = size * 0.9375  # ~600 when size=640 (matches the main view box width)
    ox = size / 2.0
    oy = size / 2.0
    ax, ay, az = angles_deg

    for lp, p3d, (cx, cy, cz) in built:
        path2d = Morph.project_xy3d_only(
            scale_a=scale_a,
            path=p3d,
            stage_w=stage_w,
            perspective_d=perspective_d,
            origin_x=ox,
            origin_y=oy,
            center_x=cx,
            center_y=cy,
            center_z=cz,
            angle_x=ax,
            angle_y=ay,
            angle_z=az,
            morph_per=1.0,
            mode="c",
        )

        rgba = _hex_to_rgba(lp.lc, lp.lp / 100.0)
        width_px = max(1, int(round(lp.lw)))

        n = (len(path2d.x) // 4) * 4
        for i in range(0, n, 4):
            p0 = (path2d.x[i + 0], path2d.y[i + 0])
            p1 = (path2d.x[i + 1], path2d.y[i + 1])
            p2 = (path2d.x[i + 2], path2d.y[i + 2])
            p3 = (path2d.x[i + 3], path2d.y[i + 3])
            pts = _sample_cubic_bezier(p0, p1, p2, p3, steps=24)
            draw.line(pts, fill=rgba, width=width_px)

    img.save(out_path)


from PIL import Image, ImageDraw

def _ease_cos_01(t: float) -> float:
    # matches JS: (cos((1-a)*PI)+1)/2
    t = max(0.0, min(1.0, t))
    return (math.cos((1.0 - t) * math.pi) + 1.0) * 0.5


def _morph_color_hex(c0: str, c1: str, per: float) -> str:
    per = max(0.0, min(1.0, per))
    c0 = (c0 or "").strip().lstrip("#")
    c1 = (c1 or "").strip().lstrip("#")
    if len(c0) != 6:
        c0 = "000000"
    if len(c1) != 6:
        c1 = "000000"
    r0, g0, b0 = int(c0[0:2], 16), int(c0[2:4], 16), int(c0[4:6], 16)
    r1, g1, b1 = int(c1[0:2], 16), int(c1[2:4], 16), int(c1[4:6], 16)
    r = round(r0 + (r1 - r0) * per)
    g = round(g0 + (g1 - g0) * per)
    b = round(b0 + (b1 - b0) * per)
    return f"{r:02X}{g:02X}{b:02X}"


def _draw_background_with_grid(
    img: Image.Image,
    background_hex: str,
    grid_hex: str,
    stage_width: int = 320,
) -> None:
    w, h = img.size
    draw = ImageDraw.Draw(img, "RGBA")

    draw.rectangle([0, 0, w, h], fill=_hex_to_rgba(background_hex, 1.0))

    bg = background_hex.strip().lstrip("#").lower()
    gg = grid_hex.strip().lstrip("#").lower()
    if bg != gg:
        # matches clsAnime.sbDrawStage grid spacing:
        # for b=0..stageWidth/10 => positions are evenly spread
        step = int(w / (stage_width / 10.0))
        col = _hex_to_rgba(grid_hex, 1.0)
        for x in range(0, w + 1, step):
            draw.line([(x, 0), (x, h)], fill=col, width=1)
            draw.line([(0, x), (w, x)], fill=col, width=1)


def render_gif_from_txtcsv(
    txtcsv: str,
    out_path: str,
    size: int = 640,
    fps: int = 20,
    background_hex: str = "111111",
    grid_hex: str = "444444",
    show_all_layers: bool = False,
    seconds_per_layer: Optional[float] = None,  # if None, uses each layer's as_ value
    supersample: int = 2,  # 1 = faster, 2 = smoother
) -> None:
    """
    Exports an animated GIF using the same camera keyframes as main_u3d.js:
    ShapeInkei.aiAutoX/Y/Z define 5 keyframes => 4 segments.
    Segment 0 uses morph_per = -ease (like JS) and color fades from white -> lc.
    Other segments use morph_per = 1.

    If show_all_layers=False: cycles layers like the website.
    If show_all_layers=True: renders all layers every frame.
    """
    layers = parse_txtcsv_layers(txtcsv)
    if not layers:
        raise ValueError("No layers parsed from txtCsv")

    # Precompute 3D paths/centers
    stage_w = float(ShapeInkei.iStageWidth)
    built = []
    for lp in layers:
        p3d = ShapeInkei.get_path3d(lp.p0, lp.p1, lp.p2, lp.p3, lp.p4, lp.p5, lp.p6, lp.p7, lp.p8, lp.p9)
        open3d = ShapeInkei.get_path3d(lp.p0, lp.p1, lp.p2, lp.p3, lp.p4, lp.p5, lp.p6, lp.p7, lp.p8, lp.p9, mode="click")
        cx, cy, cz = Morph.center_path3d(p3d)
        built.append((lp, p3d, open3d, (cx, cy, cz)))

    # Perspective like JS: iPerspective = 2 * max(fnGetPerspectiveSize3d(...))
    persp_size = 1.0
    for _, p3d, _, _ in built:
        persp_size = max(persp_size, Morph.get_perspective_size3d(size * supersample, p3d, stage_w))
    perspective_d = 2.0 * persp_size

    # Label box area size on the site is less than full panel; approximate by scale factor
    scale_a = (size * supersample) * 0.9375
    ox = (size * supersample) / 2.0
    oy = (size * supersample) / 2.0

    # Camera keyframes
    ax = ShapeInkei.aiAutoX
    ay = ShapeInkei.aiAutoY
    az = ShapeInkei.aiAutoZ
    if not (len(ax) == len(ay) == len(az) and len(ax) >= 2):
        raise ValueError("Invalid aiAutoX/Y/Z keyframes")

    segments = len(ax) - 1  # typically 4

    frames: List[Image.Image] = []

    def draw_paths_for_frame(draw_img: Image.Image, layer_indices: List[int], angle_x, angle_y, angle_z, seg_idx, seg_t):
        # seg_t is eased 0..1
        draw = ImageDraw.Draw(draw_img, "RGBA")
        for li in layer_indices:
            lp, p3d, _open3d, (cx, cy, cz) = built[li]

            # JS uses l=-a only for segment 0
            morph_per = -seg_t if seg_idx == 0 else 1.0

            # JS fades line color from white -> lc during segment 0
            lc = _morph_color_hex("FFFFFF", lp.lc, seg_t) if seg_idx == 0 else lp.lc

            path2d = Morph.project_xy3d_only(
                scale_a=scale_a,
                path=p3d,
                stage_w=stage_w,
                perspective_d=perspective_d,
                origin_x=ox,
                origin_y=oy,
                center_x=cx,
                center_y=cy,
                center_z=cz,
                angle_x=angle_x,
                angle_y=angle_y,
                angle_z=angle_z,
                morph_per=morph_per,
                mode="c",
            )

            rgba = _hex_to_rgba(lc, lp.lp / 100.0)
            width_px = max(1, int(round(lp.lw * supersample)))

            n = (len(path2d.x) // 4) * 4
            for i in range(0, n, 4):
                p0 = (path2d.x[i + 0], path2d.y[i + 0])
                p1 = (path2d.x[i + 1], path2d.y[i + 1])
                p2 = (path2d.x[i + 2], path2d.y[i + 2])
                p3 = (path2d.x[i + 3], path2d.y[i + 3])
                pts = _sample_cubic_bezier(p0, p1, p2, p3, steps=24)
                draw.line(pts, fill=rgba, width=width_px)

    # Build animation frames
    for layer_idx in range(1 if show_all_layers else len(built)):
        # choose which layers to draw per frame
        if show_all_layers:
            layer_indices = list(range(len(built)))
        else:
            layer_indices = [layer_idx]

        # duration control: mimic site "as_" seconds per layer
        layer_seconds = float(seconds_per_layer) if seconds_per_layer is not None else float(built[layer_idx][0].as_)
        layer_seconds = max(0.2, layer_seconds)

        frames_per_segment = max(2, int(round((layer_seconds * fps) / segments)))

        for seg in range(segments):
            for fi in range(frames_per_segment):
                t_lin = (fi + 1) / frames_per_segment
                t = _ease_cos_01(t_lin)

                angle_x = ax[seg] + (ax[seg + 1] - ax[seg]) * t
                angle_y = ay[seg] + (ay[seg + 1] - ay[seg]) * t
                angle_z = az[seg] + (az[seg + 1] - az[seg]) * t

                img = Image.new("RGBA", (size * supersample, size * supersample), (0, 0, 0, 0))
                _draw_background_with_grid(img, background_hex, grid_hex, stage_width=ShapeInkei.iStageWidth)
                draw_paths_for_frame(img, layer_indices, angle_x, angle_y, angle_z, seg, t)

                if supersample > 1:
                    img = img.resize((size, size), resample=Image.Resampling.LANCZOS)

                # Quantize to keep GIF size reasonable
                frames.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=256))

    duration_ms = int(round(1000 / fps))
    frames[0].save(
        out_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration_ms,
        loop=0,
        optimize=False,
        disposal=2,
    )
if __name__ == "__main__":
    txtcsv = "~p0220~p1143~p216~p36~p41~p5119~p675~lcFF3737~q0THE GLITTER APACHE REVOLVER~q1A&#39;s Penis~q2Ability : 30%"

    render_gif_from_txtcsv(
        txtcsv,
        out_path="animation.gif",
        size=640,
        fps=20,
        show_all_layers=False,   # like the site: cycles layers
        supersample=2,
    )