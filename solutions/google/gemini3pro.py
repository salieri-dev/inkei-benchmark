import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import random
import string

class InkeiAnalyzer:
    def __init__(self):
        # Constants from orig_inkei.js
        self.I_KUKI0 = 0
        self.I_KUKI1 = 3
        self.I_KITO0 = 6
        self.I_KITO1 = 9
        self.I_RINKO = 12
        self.I_KITO2 = 15
        self.I_KITO3 = 18
        self.I_KUKI2 = 21
        self.I_KUKI3 = 24

        # Base shape constants (control points) from orig_inkei.js
        # 0-12 represents the top profile, 13-24 represents the bottom/return profile
        self.base_aiX = [0,29,55,84,86,89,91,92,93,96,105,124,129,128,123,116,113,113,111,109,106,103,66,34,0]
        self.base_aiY = [0,2,3,1,2,2,4,2,0,-3,0,1,13,21,29,32,31,31,30,31,32,33,36,35,35]

    def generate_random_params(self):
        """
        Generates random parameters using Gaussian distribution centered around
        typical anatomical averages defined in the original game defaults.
        This prevents 'weird' blocky or spherical shapes.
        """
        def get_val(default, sigma, min_v, max_v):
            # Random value on bell curve centered at 'default'
            val = random.gauss(default, sigma)
            # Clamp to hard limits
            return int(max(min_v, min(val, max_v)))

        # Defaults taken from iDefXX in orig_inkei.js
        # Sigma determines how much variation is allowed (standard deviation)
        
        p0 = get_val(140, 35, 60, 280)    # Length (mm)
        
        # Circumference depends slightly on length to prevent needles or pancakes
        avg_circ = 120 + (p0 - 140) * 0.2 
        p1 = get_val(avg_circ, 25, 60, 200)   # Circumference (mm)
        
        p2 = get_val(10, 15, -30, 45)     # Shaft Curve (deg)
        p3 = get_val(10, 10, -20, 40)     # Shaft Angle (deg)
        p4 = get_val(0, 5, -15, 15)       # Glans Angle (deg)
        
        p5 = get_val(100, 10, 85, 140)    # Shaft Expansion (%) - kept tight to avoid balloons
        p6 = get_val(100, 10, 80, 130)    # Glans Expansion (%)
        
        # Pick from a palette of "Spec" colors used in the tool (Reds, Pinks, Browns)
        colors = [
            'FF3737', 'FF8888', 'FFAAAA', 'DDAA99', 'CC8877', 
            'E58E73', 'FF6666', 'CD5C5C', 'F08080', 'FA8072'
        ]
        color = random.choice(colors)
        
        name = ''.join(random.choices(string.ascii_uppercase, k=3))
        
        # Generate a funny title based on stats
        prefix = "ULTIMATE" if p0 > 180 else "NEO" if p0 < 100 else "THE"
        suffix = "DESTROYER" if p1 > 150 else "LANCE" if p0 > 160 else "CANNON"
        title = f"{prefix} {name} {suffix}"
        
        return {
            'p0': p0, 'p1': p1, 'p2': p2, 'p3': p3, 
            'p4': p4, 'p5': p5, 'p6': p6,
            'color': color,
            'name': name,
            'title': title,
            'desc': f"Ability : {random.randint(10, 99)}%"
        }

    def rotate_point(self, base_x, base_y, x, y, angle_deg):
        if angle_deg % 360 != 0:
            rad = math.radians(angle_deg)
            dx = x - base_x
            dy = y - base_y
            r = math.sqrt(dx*dx + dy*dy)
            current_angle = math.atan2(dy, dx)
            new_angle = current_angle + rad
            x = base_x + math.cos(new_angle) * r
            y = base_y + math.sin(new_angle) * r
        return x, y

    def get_2d_profile(self, p0, p1, p2, p3, p4, p5, p6):
        # Deep copy
        aiX = list(self.base_aiX)
        aiY = list(self.base_aiY)

        iAl = p0
        iRf = p1
        iSv = -p2 
        iSa = -p3
        iHa = -p4
        iSe = p5
        iHe = p6

        # 1. Height scaling (Diameter calculation)
        iChokei = iRf / math.pi
        denom = aiY[self.I_KUKI3] - aiY[self.I_KUKI0]
        iPr = iChokei / denom if denom != 0 else 1

        for i in range(len(aiY)):
            aiY[i] *= iPr

        # 2. Width/Neck scaling
        kuki0_x = aiX[self.I_KUKI0]
        kuki1_x = aiX[self.I_KUKI1]
        rinko_x = aiX[self.I_RINKO]
        
        check_val = rinko_x + (kuki1_x - rinko_x) * iPr
        limit_val = kuki0_x + (rinko_x - kuki0_x) * 0.1
        
        if check_val < limit_val:
             iPr = (kuki0_x + (rinko_x - kuki0_x) * 1.0) / (rinko_x - kuki1_x)

        for i in range(self.I_KUKI1, self.I_KUKI2 + 1):
            aiX[i] = aiX[self.I_RINKO] + (aiX[i] - aiX[self.I_RINKO]) * iPr

        # 3. Glans expansion
        cx = aiX[self.I_KITO0] + (aiX[self.I_KITO3] - aiX[self.I_KITO0]) * 0.5
        cy = aiY[self.I_KITO0] + (aiY[self.I_KITO3] - aiY[self.I_KITO0]) * 0.5
        for i in range(self.I_KITO1 - 1, self.I_KITO2 + 2):
            aiX[i] = cx + (aiX[i] - cx) * (iHe / 100.0)
            aiY[i] = cy + (aiY[i] - cy) * (iHe / 100.0)

        # 4. Shaft expansion
        cx = aiX[self.I_KUKI0] + (aiX[self.I_KUKI2] - aiX[self.I_KUKI0]) * 0.5
        cy = aiY[self.I_KUKI0] + (aiY[self.I_KUKI2] - aiY[self.I_KUKI0]) * 0.5
        for i in range(self.I_KUKI0 + 1, self.I_KUKI3):
             if i <= self.I_KUKI1 - 1 or i >= self.I_KUKI2 + 1:
                aiX[i] = cx + (aiX[i] - cx) * (iSe / 100.0)
                aiY[i] = cy + (aiY[i] - cy) * (iSe / 100.0)

        # 5. Length scaling
        denom_len = aiX[self.I_RINKO] - aiX[self.I_KUKI0]
        iPr = iAl / denom_len if denom_len != 0 else 1
        tip_x = aiX[self.I_RINKO] * iPr
        width_diff = tip_x - aiX[self.I_RINKO]
        for i in range(self.I_KUKI1, self.I_KUKI2 + 1):
            aiX[i] += width_diff

        for i in range(1, 3):
            aiX[self.I_KUKI0 + i] = aiX[self.I_KUKI0] + (aiX[self.I_KUKI1] - aiX[self.I_KUKI0]) * i / 3.0
            aiX[self.I_KUKI3 - i] = aiX[self.I_KUKI3] + (aiX[self.I_KUKI2] - aiX[self.I_KUKI3]) * i / 3.0

        # 6. Curve (Warpage)
        cx = aiX[self.I_KUKI0 + 1] + (aiX[self.I_KUKI0 + 2] - aiX[self.I_KUKI0 + 1]) * 0.5
        cy = aiY[self.I_KUKI0 + 1] + (aiY[self.I_KUKI0 + 2] - aiY[self.I_KUKI0 + 1]) * 0.5
        ir = math.sqrt(cx**2 + cy**2)
        is_angle = math.atan2(cy, cx) * (180 / math.pi)
        is_angle -= iSv
        ih = cy - (math.sin(math.radians(is_angle)) * ir)
        for i in range(self.I_KUKI0 + 1, self.I_KUKI3):
            if i <= self.I_KUKI1 - 1 or i >= self.I_KUKI2 + 1:
                aiY[i] += ih
        # Scale Y at ends due to warp
        isv_per = (1 / math.cos(math.radians(iSv))) if math.cos(math.radians(iSv)) != 0 else 1
        isv_per = (isv_per - 1) * 0.5 + 1
        aiY[self.I_KUKI0] *= isv_per
        aiY[self.I_KUKI3] *= isv_per

        # 7. Rotate neck
        cx = aiX[self.I_KUKI1] + (aiX[self.I_KUKI2] - aiX[self.I_KUKI1]) * 0.5
        cy = aiY[self.I_KUKI1] + (aiY[self.I_KUKI2] - aiY[self.I_KUKI1]) * 0.5
        for i in range(self.I_KUKI1, self.I_KUKI2 + 1):
            aiX[i], aiY[i] = self.rotate_point(cx, cy, aiX[i], aiY[i], -iSv)

        # 8. Base Rotation
        base_x = aiX[self.I_KUKI0]
        base_y = aiY[self.I_KUKI0]
        for i in range(self.I_KUKI0 + 1, self.I_KUKI3):
            aiX[i], aiY[i] = self.rotate_point(base_x, base_y, aiX[i], aiY[i], -iSa)
        isa_per = (1 / math.cos(math.radians(iSa))) if math.cos(math.radians(iSa)) != 0 else 1
        aiY[self.I_KUKI0] *= isa_per
        aiY[self.I_KUKI3] *= isa_per

        # 9. Glans Angle
        cx = aiX[self.I_KITO1] + (aiX[self.I_KITO2] - aiX[self.I_KITO1]) * 0.5
        cy = aiY[self.I_KITO1] + (aiY[self.I_KITO2] - aiY[self.I_KITO1]) * 0.5
        for i in range(self.I_RINKO - 1, self.I_RINKO + 2):
            aiX[i], aiY[i] = self.rotate_point(cx, cy, aiX[i], aiY[i], -iHa)

        # 10. Center vertically
        total_h = aiY[self.I_KUKI3] - aiY[self.I_KUKI0]
        for i in range(len(aiY)):
            aiY[i] -= total_h * 0.5

        return aiX, aiY

    def generate_3d_mesh(self, aiX, aiY, segments=16):
        """
        Revolves the 2D profile to create a 3D wireframe/mesh.
        """
        mesh_x = []
        mesh_y = []
        mesh_z = []
        step_angle = 360.0 / segments
        
        # Iterate half profile (0 to 12)
        for i in range(13):
            opp_idx = 24 - i
            # Spine Center (average of top and bottom profile points)
            cx = (aiX[i] + aiX[opp_idx]) * 0.5
            cy = (aiY[i] + aiY[opp_idx]) * 0.5
            
            # Radius Vector (from spine to top surface)
            vx = aiX[i] - cx
            vy = aiY[i] - cy
            radius = math.sqrt(vx**2 + vy**2)
            
            ring_x = []
            ring_y = []
            ring_z = []
            
            for s in range(segments):
                theta = math.radians(s * step_angle)
                # Revolve: X is along length, Y/Z are cross section
                px = cx
                py = cy + radius * math.cos(theta)
                pz = radius * math.sin(theta)
                
                ring_x.append(px)
                ring_y.append(py)
                ring_z.append(pz)
                
            mesh_x.append(ring_x)
            mesh_y.append(ring_y)
            mesh_z.append(ring_z)
            
        return np.array(mesh_x), np.array(mesh_y), np.array(mesh_z)

    def project_and_draw_wireframe(self, ax, mesh_x, mesh_y, mesh_z, color):
        # View Angles (3/4 View)
        pitch = math.radians(0) 
        yaw = math.radians(20) 
        roll = math.radians(-15) 
        
        # Rotation Matrices
        Rx = np.array([[1, 0, 0],
                       [0, math.cos(roll), -math.sin(roll)],
                       [0, math.sin(roll), math.cos(roll)]])
        Ry = np.array([[math.cos(yaw), 0, math.sin(yaw)],
                       [0, 1, 0],
                       [-math.sin(yaw), 0, math.cos(yaw)]])
        Rz = np.array([[math.cos(pitch), -math.sin(pitch), 0],
                       [math.sin(pitch), math.cos(pitch), 0],
                       [0, 0, 1]])
        R = Rz @ Ry @ Rx
        
        rows, cols = mesh_x.shape
        
        # Flatten, Rotate, Reshape
        points = np.vstack((mesh_x.flatten(), mesh_y.flatten(), mesh_z.flatten()))
        rotated = R @ points
        
        rx = rotated[0, :].reshape(rows, cols)
        ry = rotated[1, :].reshape(rows, cols)
        rz = rotated[2, :].reshape(rows, cols)
        
        # Perspective Projection
        d = 1000 
        center_x = np.mean(rx)
        center_y = np.mean(ry)
        
        proj_x = (rx - center_x) * d / (rz + d) + center_x
        proj_y = (ry - center_y) * d / (rz + d) + center_y
        
        # Convert hex color to RGB
        rgb = [int(color[i:i+2], 16)/255.0 for i in (0, 2, 4)]
        
        # 1. Draw Longitudinal Lines (Bezier strips along the length)
        # Segments map to control points in aiX array:
        # 0-3 (Root to Shaft), 3-6 (Shaft), 6-9 (Neck/Glans Base), 9-12 (Tip)
        segments_idx = [(0, 3), (3, 6), (6, 9), (9, 12)]
        
        for c in range(cols):
            verts = []
            codes = []
            
            # Move to start
            verts.append((proj_x[0, c], proj_y[0, c]))
            codes.append(Path.MOVETO)
            
            # Curve segments
            for start_idx, end_idx in segments_idx:
                for k in range(start_idx + 1, end_idx + 1):
                    verts.append((proj_x[k, c], proj_y[k, c]))
                    codes.append(Path.CURVE4)
            
            path = Path(verts, codes)
            
            # Wireframe style
            patch = patches.PathPatch(path, facecolor='none', edgecolor=rgb, lw=1.0, alpha=0.7)
            ax.add_patch(patch)

        # 2. Draw Latitudinal Lines (Rings)
        # Draw rings only at Anchor points (0, 3, 6, 9, 12) to avoid clutter
        anchor_rows = [0, 3, 6, 9, 12]
        
        for r in anchor_rows:
            ring_pts_x = []
            ring_pts_y = []
            for c in range(cols):
                ring_pts_x.append(proj_x[r, c])
                ring_pts_y.append(proj_y[r, c])
            
            # Close loop
            ring_pts_x.append(proj_x[r, 0])
            ring_pts_y.append(proj_y[r, 0])
            
            # Plot Ring
            ax.plot(ring_pts_x, ring_pts_y, color=rgb, linewidth=1.0, alpha=0.7)

        # Set Limits & Aspect Ratio
        ax.set_xlim(np.min(proj_x) - 40, np.max(proj_x) + 40)
        ax.set_ylim(np.min(proj_y) - 40, np.max(proj_y) + 40)
        ax.set_aspect('equal')
        ax.axis('off')

def main():
    analyzer = InkeiAnalyzer()
    
    # Generate "Anatomically Reasonable" Random Parameters
    params = analyzer.generate_random_params()
    print("="*30)
    print(f" ANALYZING: {params['name']}")
    print("="*30)
    print(f" Length: {params['p0']}mm")
    print(f" Girth:  {params['p1']}mm")
    print(f" Curve:  {params['p2']} deg")
    print(f" Color:  #{params['color']}")
    print("="*30)

    # 1. Generate 2D Bezier Profile
    aiX, aiY = analyzer.get_2d_profile(
        params['p0'], params['p1'], params['p2'], params['p3'], 
        params['p4'], params['p5'], params['p6']
    )
    
    # 2. Generate 3D Mesh Points (16 segments for grid look)
    mx, my, mz = analyzer.generate_3d_mesh(aiX, aiY, segments=16)
    
    # 3. Setup Plot
    bg_color = '#222222'
    fig, ax = plt.figure(figsize=(8, 10), facecolor=bg_color), plt.gca()
    ax.set_facecolor(bg_color)
    
    # 4. Render Wireframe
    analyzer.project_and_draw_wireframe(ax, mx, my, mz, params['color'])
    
    # 5. Add Info Text
    text_color = params['color'] if params['color'] != '000000' else 'white'
    
    plt.text(0.5, 0.20, f"Length : {params['p0']}mm", transform=fig.transFigure, color='white', ha='right', fontsize=10, fontfamily='monospace')
    dia = int(params['p1'] / math.pi)
    plt.text(0.5, 0.18, f"Diameter : φ{dia}mm", transform=fig.transFigure, color='white', ha='right', fontsize=10, fontfamily='monospace')
    plt.text(0.5, 0.16, f"Shaft Curve : {params['p2']}°", transform=fig.transFigure, color='white', ha='right', fontsize=10, fontfamily='monospace')
    
    plt.text(0.1, 0.08, params['title'], transform=fig.transFigure, color=f"#{text_color}", ha='left', fontsize=14, weight='bold', fontfamily='sans-serif')
    plt.text(0.1, 0.05, f"{params['name']}'s Penis", transform=fig.transFigure, color='white', ha='left', fontsize=12, fontfamily='sans-serif')
    plt.text(0.1, 0.03, params['desc'], transform=fig.transFigure, color='white', ha='left', fontsize=12, fontfamily='sans-serif')

    # Correct visual orientation
    ax.invert_yaxis()
    
    plt.tight_layout()
    output_file = f"inkei_gen_{params['name']}.png"
    plt.savefig(output_file, dpi=100, bbox_inches='tight', facecolor=bg_color)
    print(f"Image saved to {output_file}")
    plt.show()

if __name__ == "__main__":
    main()