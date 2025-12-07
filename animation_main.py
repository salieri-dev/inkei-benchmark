import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
from matplotlib.path import Path
import random
import string

class InkeiAnimator:
    def __init__(self):
        # Base profile points (25 points, indices 0-24)
        self.base_aiX = [0,29,55,84,86,89,91,92,93,96,105,124,129,128,123,116,113,113,111,109,106,103,66,34,0]
        self.base_aiY = [0,2,3,1,2,2,4,2,0,-3,0,1,13,21,29,32,31,31,30,31,32,33,36,35,35]
        
        # Index constants
        self.KUKI0 = 0   # Shaft base left
        self.KUKI1 = 3   # Shaft neck left
        self.KITO0 = 6   # Glans base left
        self.KITO1 = 9   # Glans mid left
        self.RINKO = 12  # Tip
        self.KITO2 = 15  # Glans mid right
        self.KITO3 = 18  # Glans base right
        self.KUKI2 = 21  # Shaft neck right
        self.KUKI3 = 24  # Shaft base right
        
        # Animation angles
        self.aiAutoX = [0, 0, 0, 90, 0]
        self.aiAutoY = [-160, -90, 180, 360, 630]
        self.aiAutoZ = [0, 0, 0, 0, 0]
        
    def rotate_point(self, base_x, base_y, x, y, angle_deg):
        """Exact port of clsShapeInkei.fnRotate"""
        if angle_deg % 360 != 0:
            r = math.sqrt((x - base_x)**2 + (y - base_y)**2)
            s = math.degrees(math.atan2(y - base_y, x - base_x))
            s += angle_deg
            x = base_x + math.cos(math.radians(s)) * r
            y = base_y + math.sin(math.radians(s)) * r
        return x, y
    
    def get_2d_profile(self, params):
        """Exact port of clsShapeInkei.fnGetPath()"""
        aiX = list(self.base_aiX)
        aiY = list(self.base_aiY)
        
        iAl = params['length']
        iRf = params['girth']
        iSv = params['curve']
        iSa = params['angle']
        iHa = params['glans_angle']
        iSe = params['shaft_exp']
        iHe = params['glans_exp']
        
        KUKI0, KUKI1, KITO0, KITO1 = self.KUKI0, self.KUKI1, self.KITO0, self.KITO1
        RINKO, KITO2, KITO3, KUKI2, KUKI3 = self.RINKO, self.KITO2, self.KITO3, self.KUKI2, self.KUKI3
        
        # Step 1: Diameter from circumference
        iChokei = iRf / math.pi
        
        # Step 2: Scale Y by diameter ratio
        iPr = iChokei / (aiY[KUKI3] - aiY[KUKI0]) if (aiY[KUKI3] - aiY[KUKI0]) != 0 else 1
        for i in range(len(aiY)):
            aiY[i] *= iPr
        
        # Step 3: Check/adjust neck geometry
        test_val = aiX[RINKO] + (aiX[KUKI1] - aiX[RINKO]) * iPr
        limit_val = aiX[KUKI0] + (aiX[RINKO] - aiX[KUKI0]) * 0.1
        if test_val < limit_val:
            denom = aiX[RINKO] - aiX[KUKI1]
            iPr = (aiX[KUKI0] + (aiX[RINKO] - aiX[KUKI0]) * 1) / denom if denom != 0 else 1
        
        # Scale X for neck/glans region
        for i in range(KUKI1, KUKI2 + 1):
            aiX[i] = aiX[RINKO] + (aiX[i] - aiX[RINKO]) * iPr
        
        # Step 4: Glans expansion (iHe)
        cx = aiX[KITO0] + (aiX[KITO3] - aiX[KITO0]) * 0.5
        cy = aiY[KITO0] + (aiY[KITO3] - aiY[KITO0]) * 0.5
        for i in range(KITO1 - 1, KITO2 + 2):
            aiX[i] = cx + (aiX[i] - cx) * (iHe / 100.0)
            aiY[i] = cy + (aiY[i] - cy) * (iHe / 100.0)
        
        # Step 5: Shaft expansion (iSe)
        cx = aiX[KUKI0] + (aiX[KUKI2] - aiX[KUKI0]) * 0.5
        cy = aiY[KUKI0] + (aiY[KUKI2] - aiY[KUKI0]) * 0.5
        for i in range(KUKI0 + 1, KUKI3):
            if i <= KUKI1 - 1 or i >= KUKI2 + 1:
                aiX[i] = cx + (aiX[i] - cx) * (iSe / 100.0)
                aiY[i] = cy + (aiY[i] - cy) * (iSe / 100.0)
        
        # Step 6: Length scale (iAl)
        denom = aiX[RINKO] - aiX[KUKI0]
        iPr = iAl / denom if denom != 0 else 1
        iX_new = aiX[RINKO] * iPr
        iW = iX_new - aiX[RINKO]
        
        for i in range(KUKI1, KUKI2 + 1):
            aiX[i] += iW
        
        # Adjust shaft control points
        for i in range(1, 3):
            aiX[KUKI0 + i] = aiX[KUKI0] + (aiX[KUKI1] - aiX[KUKI0]) * i / 3.0
            aiX[KUKI3 - i] = aiX[KUKI3] + (aiX[KUKI2] - aiX[KUKI3]) * i / 3.0
        
        # Step 7: Shaft curve (iSv)
        iX = aiX[KUKI0 + 1] + (aiX[KUKI0 + 2] - aiX[KUKI0 + 1]) * 0.5
        iY = aiY[KUKI0 + 1] + (aiY[KUKI0 + 2] - aiY[KUKI0 + 1]) * 0.5
        iR = math.sqrt(iX**2 + iY**2)
        iS = math.degrees(math.atan2(iY, iX))
        iS -= iSv
        iH = iY - math.sin(math.radians(iS)) * iR
        
        for i in range(KUKI0 + 1, KUKI3):
            if i <= KUKI1 - 1 or i >= KUKI2 + 1:
                aiY[i] += iH
        
        # Base expansion due to curve
        if abs(iSv) < 89:
            iSvStEdHPer = 1.0 / math.cos(math.radians(iSv))
            iSvStEdHPer = (iSvStEdHPer - 1) * 0.5 + 1
            aiY[KUKI0] *= iSvStEdHPer
            aiY[KUKI3] *= iSvStEdHPer
        
        # Rotate neck/glans by curve
        cx = aiX[KUKI1] + (aiX[KUKI2] - aiX[KUKI1]) * 0.5
        cy = aiY[KUKI1] + (aiY[KUKI2] - aiY[KUKI1]) * 0.5
        for i in range(KUKI1, KUKI2 + 1):
            aiX[i], aiY[i] = self.rotate_point(cx, cy, aiX[i], aiY[i], -iSv)
        
        # Step 8: Shaft angle (iSa)
        px, py = aiX[KUKI0], aiY[KUKI0]
        for i in range(KUKI0 + 1, KUKI3):
            aiX[i], aiY[i] = self.rotate_point(px, py, aiX[i], aiY[i], -iSa)
        
        # Base expansion due to angle
        if abs(iSa) < 89:
            iSaStEdHPer = 1.0 / math.cos(math.radians(iSa))
            aiY[KUKI0] *= iSaStEdHPer
            aiY[KUKI3] *= iSaStEdHPer
        
        # Step 9: Glans angle (iHa)
        cx = aiX[KITO1] + (aiX[KITO2] - aiX[KITO1]) * 0.5
        cy = aiY[KITO1] + (aiY[KITO2] - aiY[KITO1]) * 0.5
        for i in range(RINKO - 1, RINKO + 2):
            aiX[i], aiY[i] = self.rotate_point(cx, cy, aiX[i], aiY[i], -iHa)
        
        # Step 10: Center Y axis
        iH = aiY[KUKI3] - aiY[KUKI0]
        for i in range(len(aiY)):
            aiY[i] -= iH * 0.5
        
        return aiX, aiY
    
    def convert_to_3d_cylinder(self, aiX, aiY, num_segments=12):
        """
        Improved 3D conversion with Anti-Twist logic.
        Ensures the cross-section orientation doesn't flip 180 degrees
        when curvature causes the profile top/bottom to cross.
        """
        num_positions = 13
        
        mesh_x = np.zeros((num_positions, num_segments))
        mesh_y = np.zeros((num_positions, num_segments))
        mesh_z = np.zeros((num_positions, num_segments))
        
        # Variables to track previous orientation vector
        prev_rx, prev_ry = 0.0, 0.0
        
        for pos in range(num_positions):
            top_idx = pos
            bottom_idx = 24 - pos
            
            # Calculate the center point
            cx = (aiX[top_idx] + aiX[bottom_idx]) * 0.5
            cy = (aiY[top_idx] + aiY[bottom_idx]) * 0.5
            
            # Calculate the radius vector (Center -> Top)
            # This determines the tilt of the cross-section
            rx = aiX[top_idx] - cx
            ry = aiY[top_idx] - cy
            
            # ANTI-TWIST LOGIC:
            # If the vector flips direction (>90 deg change) compared to previous segment,
            # negate it to maintain mesh topology winding.
            if pos > 0:
                dot_prod = rx * prev_rx + ry * prev_ry
                # If dot product is negative, vectors are opposing.
                # Check magnitudes to ensure we aren't just crossing a zero-point at the tip.
                mag_curr = math.sqrt(rx**2 + ry**2)
                mag_prev = math.sqrt(prev_rx**2 + prev_ry**2)
                
                if dot_prod < 0 and mag_curr > 0.01 and mag_prev > 0.01:
                    rx = -rx
                    ry = -ry
            
            # Store current valid vector for next iteration check
            prev_rx, prev_ry = rx, ry
            
            radius = math.sqrt(rx**2 + ry**2)
            
            # Handle tip singularity or collapsed sections
            if radius < 0.01:
                # Collapse to center point
                for seg in range(num_segments):
                    mesh_x[pos, seg] = cx
                    mesh_y[pos, seg] = cy
                    mesh_z[pos, seg] = 0
            else:
                for seg in range(num_segments):
                    theta = math.radians(270 + seg * (360.0 / num_segments))
                    sin_t = math.sin(theta) # Controls position along cut line
                    cos_t = math.cos(theta) # Controls depth (Z)
                    
                    mesh_x[pos, seg] = cx + (rx * sin_t)
                    mesh_y[pos, seg] = cy + (ry * sin_t)
                    mesh_z[pos, seg] = radius * cos_t
        
        return mesh_x, mesh_y, mesh_z
    
    def rotate_3d_point(self, x, y, z, angle_x, angle_y, angle_z):
        """Port of fnGetXY3dOnly rotation logic"""
        if angle_z % 360 != 0:
            r = math.sqrt(x**2 + y**2)
            s = math.degrees(math.atan2(y, x)) + angle_z
            x = math.cos(math.radians(s)) * r
            y = math.sin(math.radians(s)) * r
        
        if angle_x % 360 != 0:
            r = math.sqrt(y**2 + z**2)
            s = math.degrees(math.atan2(z, y)) + angle_x
            y = math.cos(math.radians(s)) * r
            z = math.sin(math.radians(s)) * r
        
        if angle_y % 360 != 0:
            r = math.sqrt(z**2 + x**2)
            s = math.degrees(math.atan2(x, z)) + (-angle_y)
            z = math.cos(math.radians(s)) * r
            x = math.sin(math.radians(s)) * r
        
        return x, y, z
    
    def project_3d_to_2d(self, mesh_x, mesh_y, mesh_z, angle_x, angle_y, angle_z,
                         center_x, center_y, center_z, perspective, offset_x, offset_y):
        """Project 3D mesh to 2D with perspective"""
        rows, cols = mesh_x.shape
        proj_x = np.zeros_like(mesh_x)
        proj_y = np.zeros_like(mesh_y)
        
        for r in range(rows):
            for c in range(cols):
                x = mesh_x[r, c] - center_x
                y = mesh_y[r, c] - center_y
                z = mesh_z[r, c] - center_z
                
                x, y, z = self.rotate_3d_point(x, y, z, angle_x, angle_y, angle_z)
                
                # Protect against zero division or extreme perspective
                if perspective == 0: perspective = 1
                scale_factor = (-z + perspective) / perspective
                
                # Project
                proj_x[r, c] = offset_x + x * scale_factor
                proj_y[r, c] = offset_y + y * scale_factor
        
        return proj_x, proj_y
    
    def ease_in_out(self, t):
        """Original easing function"""
        return (math.cos((1 - t) * math.pi) + 1) / 2


class InkeiAnalyzer:
    def __init__(self):
        self.animator = InkeiAnimator()
        self.display_scale = 1.8

    def generate_random_params(self):
        def get_val(default, sigma, min_v, max_v):
            val = random.gauss(default, sigma)
            return int(max(min_v, min(val, max_v)))

        length_mm = get_val(155, 40, 80, 280)
        avg_circ = 115 + (length_mm - 140) * 0.25 
        girth_mm = get_val(avg_circ, 25, 70, 200)
        
        curve_deg = get_val(5, 20, -25, 50)
        angle_deg = get_val(10, 15, -15, 35)
        glans_angle = get_val(0, 5, -15, 15)
        shaft_exp = get_val(105, 15, 85, 140)
        glans_exp = get_val(100, 15, 75, 135)
        
        ball_dia = get_val(45, 8, 35, 75) 
        ball_hang = get_val(girth_mm/2.0, 20, 45, 140) 

        colors = ['FF3737', 'FF8888', 'FFAAAA', 'E58E73', 'FF6666', 'CD5C5C', 'FA8072']
        color = random.choice(colors)
        name = ''.join(random.choices(string.ascii_uppercase, k=3))
        
        # Scoring
        score = 0
        notes = []

        if 130 <= length_mm <= 165: 
            score += 40
        elif length_mm < 130:
            diff = 130 - length_mm
            score += max(0, 40 - (diff * 0.8))
            if length_mm < 100: 
                notes.append("SHORT")
        else:
            diff = length_mm - 165
            score += max(-20, 40 - (diff * 1.5)) 
            if length_mm > 180: 
                notes.append("PAIN RISK (LEN)")

        if 115 <= girth_mm <= 135: 
            score += 40
        elif girth_mm < 115:
            diff = 115 - girth_mm
            score += max(0, 40 - (diff * 0.8))
            if girth_mm < 100: 
                notes.append("THIN")
        else:
            diff = girth_mm - 135
            score += max(-20, 40 - (diff * 2.0)) 
            if girth_mm > 145: 
                notes.append("PAIN RISK (GTH)")

        if 5 <= curve_deg <= 25:
            score += 20
            notes.append("G-SPOT OPTIMAL")
        elif 25 < curve_deg <= 35: 
            score += 5
        elif curve_deg > 35:
            score -= 30
            notes.append("HARD CURVE")
        elif -10 <= curve_deg < 5: 
            score += 10
        else: 
            score -= 10 

        stamina = random.randint(20, 99)
        score += (stamina / 10)

        if score > 95: rank = "S"
        elif score > 80: rank = "A"
        elif score > 60: rank = "B"
        elif score > 40: rank = "C"
        else: rank = "D" 

        if "PAIN RISK (LEN)" in notes and "PAIN RISK (GTH)" in notes: 
            class_name = "ANATOMICAL HAZARD"
        elif "PAIN RISK (LEN)" in notes: 
            class_name = "CERVIX BRUISER"
        elif "PAIN RISK (GTH)" in notes: 
            class_name = "STRETCH HAZARD"
        elif "SHORT" in notes: 
            class_name = "COMPACT UTILITY"
        elif "G-SPOT OPTIMAL" in notes and rank in ["S", "A"]: 
            class_name = "IDEAL PARTNER"
        elif rank == "S": 
            class_name = "GOLDILOCKS UNIT"
        else: 
            class_name = "STANDARD MODEL"

        radius_cm = (girth_mm / math.pi) / 10 / 2
        length_cm = length_mm / 10
        shaft_vol_cc = math.pi * (radius_cm ** 2) * length_cm
        ball_r_cm = (ball_dia / 10) / 2
        ball_vol_cc = 2 * ((4/3) * math.pi * (ball_r_cm ** 3))
        weight = shaft_vol_cc + ball_vol_cc

        base_load = random.uniform(2.0, 6.0)
        vol_bonus = ball_vol_cc * 0.12
        cum_ml = base_load + vol_bonus
        density = random.randint(40, 200)
        
        subject_id = ''.join(random.choices(string.digits, k=8))
        
        print(f"--- SUBJECT {name} ---")
        print(f"Dim: {length_mm/10}cm x {girth_mm/10}cm")
        print(f"Score: {int(score)} | Rank: {rank}")

        return {
            'length': length_mm, 'girth': girth_mm, 'curve': curve_deg, 
            'angle': angle_deg, 'glans_angle': glans_angle, 
            'shaft_exp': shaft_exp, 'glans_exp': glans_exp,
            'ball_dia': ball_dia, 'ball_hang': ball_hang,
            'color': color, 'name': name, 'subject_id': subject_id,
            'rank': rank, 'class': class_name, 
            'stamina': stamina, 'score': score, 'notes': notes,
            'volume': shaft_vol_cc, 'ball_vol': ball_vol_cc, 'weight': weight,
            'cum_ml': cum_ml, 'density': density
        }

    def create_animation(self, params, output_file='inkei_animation.gif',
                        fps=30, duration_per_phase=2.0):
        """Create the full animation with UI"""
        
        # Generate 2D profile
        aiX, aiY = self.animator.get_2d_profile(params)
        
        # Convert to 3D cylinder
        mesh_x, mesh_y, mesh_z = self.animator.convert_to_3d_cylinder(aiX, aiY, num_segments=12)
        
        # Calculate center
        center_x = np.mean(mesh_x)
        center_y = np.mean(mesh_y)
        center_z = np.mean(mesh_z)
        
        # Perspective distance
        max_extent = max(
            np.max(mesh_x) - np.min(mesh_x),
            np.max(mesh_y) - np.min(mesh_y),
            np.max(mesh_z) - np.min(mesh_z)
        )
        if max_extent == 0: max_extent = 100
        perspective = max_extent * 2
        
        # Colors
        bg_color = '#1a1a1a'
        accent_color = '#00FFFF'
        color_hex = params.get('color', 'FF3737')
        color_rgb = tuple(int(color_hex[i:i+2], 16)/255 for i in (0, 2, 4))
        main_rgb = f"#{color_hex}"
        
        # Setup figure with TIGHT UI layout
        fig = plt.figure(figsize=(12, 7), facecolor=bg_color)
        
        # Main viewport for 3D model (left side)
        ax_main = fig.add_axes([0.02, 0.02, 0.58, 0.96])
        ax_main.set_facecolor(bg_color)
        
        # Radar chart (Bottom Right Corner)
        ax_radar = fig.add_axes([0.65, 0.05, 0.30, 0.35], polar=True, facecolor='#0a0a0a')
        
        # Animation parameters
        num_phases = 4
        frames_per_phase = int(fps * duration_per_phase)
        total_frames = frames_per_phase * num_phases
        
        # Display scaling
        display_scale = self.display_scale
        offset_x = 70
        offset_y = 0
        
        # Pre-draw static UI elements
        self._draw_static_ui(fig, params, accent_color, main_rgb, bg_color)
        self._draw_radar_chart(ax_radar, params, main_rgb)
        
        def animate(frame):
            ax_main.clear()
            ax_main.set_facecolor(bg_color)
            
            # Determine phase and progress
            phase = min(frame // frames_per_phase, num_phases - 1)
            t = (frame % frames_per_phase) / frames_per_phase if phase < num_phases else 1.0
            if frame >= total_frames - 1:
                phase = num_phases - 1
                t = 1.0
            
            # Apply easing
            t_eased = self.animator.ease_in_out(t)
            
            # Interpolate angles
            angle_x = self.animator.aiAutoX[phase] + (self.animator.aiAutoX[phase + 1] - self.animator.aiAutoX[phase]) * t_eased
            angle_y = self.animator.aiAutoY[phase] + (self.animator.aiAutoY[phase + 1] - self.animator.aiAutoY[phase]) * t_eased
            angle_z = self.animator.aiAutoZ[phase] + (self.animator.aiAutoZ[phase + 1] - self.animator.aiAutoZ[phase]) * t_eased
            
            # Project to 2D
            proj_x, proj_y = self.animator.project_3d_to_2d(
                mesh_x, mesh_y, mesh_z,
                angle_x, angle_y, angle_z,
                center_x, center_y, center_z,
                perspective, offset_x, offset_y
            )
            
            # Scale for display
            proj_x *= display_scale
            proj_y *= display_scale
            
            rows, cols = proj_x.shape
            
            # Draw grid
            self._draw_grid(ax_main, accent_color)
            
            # Draw longitudinal lines
            for c in range(cols):
                x_pts = proj_x[:, c]
                y_pts = proj_y[:, c]
                ax_main.plot(x_pts, y_pts, color=color_rgb, linewidth=1.8, alpha=0.9)
            
            # Draw cross-section rings
            ring_indices = [0, 3, 6, 9, 12]
            for r in ring_indices:
                x_pts = np.append(proj_x[r, :], proj_x[r, 0])
                y_pts = np.append(proj_y[r, :], proj_y[r, 0])
                ax_main.plot(x_pts, y_pts, color=color_rgb, linewidth=1.0, alpha=0.7)
            
            # Draw tip reticle
            tip_x = np.mean(proj_x[12, :])
            tip_y = np.mean(proj_y[12, :])
            self._draw_reticle(ax_main, tip_x, tip_y, accent_color)
            
            # Set consistent view limits
            ax_main.set_xlim(-80, 380)
            ax_main.set_ylim(-150, 150)
            ax_main.set_aspect('equal')
            ax_main.axis('off')
            
            # Draw rulers
            self._draw_rulers(ax_main, accent_color, params['length'])
            
            # Draw viewport frame
            self._draw_viewport_frame(ax_main, accent_color)
            
            return []
        
        print(f"Creating animation with {total_frames} frames...")
        anim = animation.FuncAnimation(
            fig, animate, frames=total_frames,
            interval=1000/fps, blit=False
        )
        
        # Save
        if output_file.endswith('.gif'):
            print("Saving GIF (this may take a moment)...")
            anim.save(output_file, writer='pillow', fps=fps)
        elif output_file.endswith('.mp4'):
            print("Saving MP4...")
            anim.save(output_file, writer='ffmpeg', fps=fps, 
                     extra_args=['-vcodec', 'libx264', '-pix_fmt', 'yuv420p'])
        else:
            output_file += '.gif'
            anim.save(output_file, writer='pillow', fps=fps)
        
        plt.close()
        print(f"Animation saved to {output_file}")
        return output_file

    def _draw_static_ui(self, fig, params, accent_color, main_rgb, bg_color):
        """Draw all static UI elements with improved layout"""
        
        # Main Viewport Frame (Left)
        rect_frame = patches.FancyBboxPatch(
            (0.015, 0.015), 0.59, 0.97,
            transform=fig.transFigure,
            fill=False, edgecolor='#444444', linewidth=2,
            boxstyle="round,pad=0.01"
        )
        fig.add_artist(rect_frame)
        
        # Sidebar Background (Right)
        sidebar_bg = patches.FancyBboxPatch(
            (0.62, 0.015), 0.36, 0.97,
            transform=fig.transFigure,
            facecolor='#0a0a0a', alpha=0.9,
            edgecolor='#333333', linewidth=1,
            boxstyle="round,pad=0.01"
        )
        fig.add_artist(sidebar_bg)
        
        def draw_text(x, y, text, size=10, color='white', weight='normal', align='left', alpha=1.0):
            fig.text(x, y, text, color=color, fontsize=size, fontweight=weight, 
                    fontfamily='monospace', ha=align, alpha=alpha)
        
        # --- HEADER (Top Left overlay) ---
        draw_text(0.04, 0.93, f"SUBJECT: {params['name']}", size=16, weight='bold', color='white')
        draw_text(0.04, 0.90, f"ID: {params['subject_id']}", size=9, color=accent_color)
        
        # --- SAFETY CLASS (Top Center of Viewport) ---
        draw_text(0.35, 0.95, "SAFETY CLASS", size=7, color=accent_color, align='center')
        
        class_box = patches.FancyBboxPatch(
            (0.25, 0.89), 0.20, 0.05,
            transform=fig.transFigure,
            facecolor='#1a1a1a', alpha=0.8,
            edgecolor=accent_color, linewidth=1,
            boxstyle="round,pad=0.01"
        )
        fig.add_artist(class_box)
        draw_text(0.35, 0.905, params['class'], size=10, weight='bold', color='white', align='center')
        
        # --- PARTNER GRADE (Bottom Left overlay) ---
        rank_colors = {'S': '#00FF7F', 'A': '#1E90FF', 'B': '#FFD700', 'C': '#FF8C00', 'D': '#FF4444'}
        rc = rank_colors.get(params['rank'], 'white')
        
        badge_x, badge_y = 0.04, 0.04
        rank_box_outer = patches.FancyBboxPatch(
            (badge_x, badge_y), 0.08, 0.15,
            transform=fig.transFigure,
            facecolor='#0a0a0a', alpha=0.9,
            edgecolor=rc, linewidth=3,
            boxstyle="round,pad=0.01"
        )
        fig.add_artist(rank_box_outer)
        
        draw_text(badge_x + 0.04, badge_y + 0.12, "GRADE", size=7, color='#888888', align='center')
        draw_text(badge_x + 0.04, badge_y + 0.02, params['rank'], size=42, weight='bold', color=rc, align='center')
        
        # --- WARNING LABELS (Top Right overlay of Viewport) ---
        warn_y = 0.92
        for note in params['notes']:
            if "PAIN" in note or "HAZARD" in note or "HARD" in note:
                c = '#FF4444'
            elif "G-SPOT" in note:
                c = '#00FF7F'
            else:
                c = '#FFD700'
            draw_text(0.58, warn_y, f"[{note}]", size=8, color=c, weight='bold', align='right')
            warn_y -= 0.025
        
        # --- SIDEBAR CONTENT (Right) ---
        sx = 0.65
        sy = 0.94
        gap = 0.03
        
        # 1. SCORE AT TOP
        draw_text(sx, sy, "/// COMPATIBILITY SCORE", size=9, color=accent_color, weight='bold')
        sy -= 0.05
        
        score_color = rank_colors.get(params['rank'], 'white')
        draw_text(sx, sy, f"{int(params['score'])}", size=26, weight='bold', color=score_color, align='left')
        draw_text(sx + 0.12, sy + 0.01, "/ 100", size=10, color='#555555')
        
        sy -= 0.06
        
        # 2. PHYSICAL METRICS
        draw_text(sx, sy, "/// ANATOMY SCAN", size=9, color=accent_color, weight='bold')
        sy -= gap * 1.5
        
        metrics_phys = [
            ("LENGTH", f"{params['length']/10:.1f}", "cm"),
            ("GIRTH", f"{params['girth']/10:.1f}", "cm"),
            ("DIAM", f"{params['girth']/math.pi/10:.1f}", "cm"),
            ("CURVE", f"{params['curve']:+d}", "deg"),
            ("ANGLE", f"{params['angle']:+d}", "deg"),
            ("BALLS", f"φ{params['ball_dia']/10:.1f}", "cm"),
        ]
        
        # Two column layout
        start_sy = sy
        for i, (label, val, unit) in enumerate(metrics_phys):
            col_offset = 0.16 if i >= 3 else 0
            row_y = start_sy - (i % 3) * gap
            
            draw_text(sx + col_offset, row_y, label, size=8, color='#666666')
            draw_text(sx + col_offset + 0.11, row_y, val, size=9, weight='bold', color=main_rgb, align='right')
            draw_text(sx + col_offset + 0.12, row_y, unit, size=8, color='#555555')

        sy = start_sy - (3 * gap) - 0.02
        
        # 3. EXPANSION & PERFORMANCE
        draw_text(sx, sy, "/// PERFORMANCE METRICS", size=9, color=accent_color, weight='bold')
        sy -= gap * 1.5
        
        metrics_misc = [
            ("SHAFT EXP", f"{params['shaft_exp']}%"),
            ("GLANS EXP", f"{params['glans_exp']}%"),
            ("STAMINA", f"{params['stamina']}/100"),
            ("LOAD VOL", f"{params['cum_ml']:.1f}mL"),
        ]
        
        for label, val in metrics_misc:
            draw_text(sx, sy, label, size=8, color='#666666')
            draw_text(sx + 0.28, sy, val, size=9, weight='bold', color='white', align='right')
            sy -= gap
            
        draw_text(sx, 0.40, "/// RADAR ANALYSIS", size=9, color=accent_color, weight='bold')

    
    def _draw_radar_chart(self, ax_radar, params, main_rgb):
        """Draw the radar chart with high contrast"""
        categories = ['LEN', 'GIRTH', 'G-SPOT', 'STAM', 'LOAD']
        
        # Calculate scores
        len_score = max(0, min(1.0, 1.0 - abs(params['length'] - 145) / 80.0))
        girth_score = max(0, min(1.0, 1.0 - abs(params['girth'] - 125) / 60.0))
        curve_score = max(0, min(1.0, 1.0 - abs(params['curve'] - 15) / 50.0))
        
        values = [
            len_score,
            girth_score,
            curve_score,
            params['stamina'] / 100.0,
            min(1, params['cum_ml'] / 12.0)
        ]
        values += values[:1]
        
        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
        angles += angles[:1]
        
        # Parse color
        color_hex = main_rgb.replace('#', '')
        color_rgb = tuple(int(color_hex[i:i+2], 16)/255 for i in (0, 2, 4))
        
        ax_radar.set_theta_offset(np.pi / 2)
        ax_radar.set_theta_direction(-1)
        
        # Draw reference circles - INCREASED OPACITY & BRIGHTNESS
        for r in [0.25, 0.5, 0.75, 1.0]:
            circle_angles = np.linspace(0, 2 * np.pi, 100)
            circle_r = np.full_like(circle_angles, r)
            ax_radar.plot(circle_angles, circle_r, color='#666666', linewidth=0.8, linestyle='--', alpha=0.8)
        
        # Draw the data - INCREASED ALPHA
        ax_radar.plot(angles, values, color=color_rgb, linewidth=2.5, linestyle='solid')
        ax_radar.fill(angles, values, color=color_rgb, alpha=0.65)
        
        # Configure axes - INCREASED CONTRAST
        ax_radar.set_yticklabels([])
        ax_radar.set_xticks(angles[:-1])
        ax_radar.set_xticklabels(categories, color='white', size=8, fontfamily='monospace', weight='bold')
        ax_radar.spines['polar'].set_color('#666666')
        ax_radar.grid(color='#555555', linestyle='--', linewidth=0.8, alpha=0.7)
        ax_radar.set_ylim(0, 1)
        ax_radar.set_facecolor('#0a0a0a')
        
        # Draw axis lines from center - INCREASED VISIBILITY
        for angle in angles[:-1]:
            ax_radar.plot([angle, angle], [0, 1], color='#666666', linewidth=0.8, alpha=0.7)
    
    def _draw_grid(self, ax, accent_color):
        """Draw background grid"""
        for x in range(-50, 400, 25):
            ax.axvline(x, color=accent_color, alpha=0.05, linewidth=0.5)
        for y in range(-150, 160, 25):
            ax.axhline(y, color=accent_color, alpha=0.05, linewidth=0.5)
    
    def _draw_rulers(self, ax, accent_color, length_mm):
        """Draw measurement rulers"""
        display_scale = self.display_scale
        pixels_per_cm = 10 * display_scale
        
        # Top ruler - horizontal
        ruler_y = 130
        max_cm = 22
        ruler_start_x = 0
        ruler_end_x = max_cm * pixels_per_cm
        
        ax.plot([ruler_start_x, ruler_end_x], [ruler_y, ruler_y], 
                color=accent_color, lw=0.8, alpha=0.4)
        
        for cm in range(0, max_cm + 1):
            x = cm * pixels_per_cm
            is_major = (cm % 5 == 0)
            lw = 1.0 if is_major else 0.5
            height = 10 if is_major else 5
            ax.plot([x, x], [ruler_y, ruler_y - height], 
                   color=accent_color, lw=lw, alpha=0.6)
            if is_major:
                ax.text(x, ruler_y + 10, f"{cm}", color=accent_color, ha='center', 
                       fontsize=8, fontfamily='monospace', alpha=0.8)
        
        ax.text(ruler_end_x + 10, ruler_y, "cm", color=accent_color, ha='left',
               fontsize=7, fontfamily='monospace', alpha=0.6, va='center')
        
        # Left ruler - vertical
        ruler_x = -50
        max_v_cm = 12
        
        ax.plot([ruler_x, ruler_x], [-max_v_cm/2 * pixels_per_cm, max_v_cm/2 * pixels_per_cm], 
                color=accent_color, lw=0.8, alpha=0.4)
        
        for cm in range(-6, 7):
            y = cm * pixels_per_cm
            is_major = (cm % 2 == 0)
            width = 10 if is_major else 5
            ax.plot([ruler_x, ruler_x + width], [y, y], 
                   color=accent_color, lw=0.5, alpha=0.6)
            if is_major:
                ax.text(ruler_x - 5, y, f"{abs(cm)}", color=accent_color, ha='right',
                       fontsize=7, fontfamily='monospace', alpha=0.7, va='center')
    
    def _draw_reticle(self, ax, x, y, color):
        """Draw targeting reticle at tip"""
        size = 15
        ax.plot([x - size, x + size], [y, y], color=color, lw=0.8, alpha=0.6)
        ax.plot([x, x], [y - size, y + size], color=color, lw=0.8, alpha=0.6)
        circle = plt.Circle((x, y), size * 0.6, fill=False, color=color, lw=0.8, alpha=0.6)
        ax.add_patch(circle)
    
    def _draw_viewport_frame(self, ax, color):
        """Draw corner brackets for viewport"""
        cs = 20
        lw = 2
        alpha = 0.5
        xl, xr = ax.get_xlim()
        yb, yt = ax.get_ylim()
        off = 10
        xl += off
        xr -= off
        yb += off
        yt -= off
        
        ax.plot([xl, xl + cs], [yt, yt], color=color, lw=lw, alpha=alpha)
        ax.plot([xl, xl], [yt, yt - cs], color=color, lw=lw, alpha=alpha)
        ax.plot([xr - cs, xr], [yt, yt], color=color, lw=lw, alpha=alpha)
        ax.plot([xr, xr], [yt, yt - cs], color=color, lw=lw, alpha=alpha)
        ax.plot([xl, xl + cs], [yb, yb], color=color, lw=lw, alpha=alpha)
        ax.plot([xl, xl], [yb, yb + cs], color=color, lw=lw, alpha=alpha)
        ax.plot([xr - cs, xr], [yb, yb], color=color, lw=lw, alpha=alpha)
        ax.plot([xr, xr], [yb, yb + cs], color=color, lw=lw, alpha=alpha)

    def generate_static_image(self, params, output_file='inkei_static.png'):
        """Generate a static image at the final pose with fixed layout"""
        
        aiX, aiY = self.animator.get_2d_profile(params)
        mesh_x, mesh_y, mesh_z = self.animator.convert_to_3d_cylinder(aiX, aiY, num_segments=12)
        
        center_x = np.mean(mesh_x)
        center_y = np.mean(mesh_y)
        center_z = np.mean(mesh_z)
        
        max_extent = max(
            np.max(mesh_x) - np.min(mesh_x),
            np.max(mesh_y) - np.min(mesh_y),
            np.max(mesh_z) - np.min(mesh_z)
        )
        if max_extent == 0: max_extent = 100
        perspective = max_extent * 2
        
        bg_color = '#1a1a1a'
        accent_color = '#00FFFF'
        color_hex = params.get('color', 'FF3737')
        color_rgb = tuple(int(color_hex[i:i+2], 16)/255 for i in (0, 2, 4))
        main_rgb = f"#{color_hex}"
        
        # Match animation figure size
        fig = plt.figure(figsize=(12, 7), facecolor=bg_color)
        
        # Match animation axes positions
        ax_main = fig.add_axes([0.02, 0.02, 0.58, 0.96])
        ax_main.set_facecolor(bg_color)
        
        ax_radar = fig.add_axes([0.65, 0.05, 0.30, 0.35], polar=True, facecolor='#0a0a0a')
        
        # Face East (0 deg) for static image
        angle_x = 0
        angle_y = 0
        angle_z = 0
        
        display_scale = self.display_scale
        offset_x = 70
        offset_y = 0
        
        proj_x, proj_y = self.animator.project_3d_to_2d(
            mesh_x, mesh_y, mesh_z,
            angle_x, angle_y, angle_z,
            center_x, center_y, center_z,
            perspective, offset_x, offset_y
        )
        
        proj_x *= display_scale
        proj_y *= display_scale
        
        rows, cols = proj_x.shape
        
        self._draw_static_ui(fig, params, accent_color, main_rgb, bg_color)
        self._draw_radar_chart(ax_radar, params, main_rgb)
        self._draw_grid(ax_main, accent_color)
        
        for c in range(cols):
            ax_main.plot(proj_x[:, c], proj_y[:, c], color=color_rgb, linewidth=1.8, alpha=0.9)
        
        ring_indices = [0, 3, 6, 9, 12]
        for r in ring_indices:
            x_pts = np.append(proj_x[r, :], proj_x[r, 0])
            y_pts = np.append(proj_y[r, :], proj_y[r, 0])
            ax_main.plot(x_pts, y_pts, color=color_rgb, linewidth=1.0, alpha=0.7)
        
        tip_x = np.mean(proj_x[12, :])
        tip_y = np.mean(proj_y[12, :])
        self._draw_reticle(ax_main, tip_x, tip_y, accent_color)
        
        ax_main.set_xlim(-80, 380)
        ax_main.set_ylim(-150, 150)
        ax_main.set_aspect('equal')
        ax_main.axis('off')
        
        self._draw_rulers(ax_main, accent_color, params['length'])
        self._draw_viewport_frame(ax_main, accent_color)
        
        plt.savefig(output_file, dpi=150, bbox_inches='tight', facecolor=bg_color)
        plt.close()
        print(f"Static image saved to {output_file}")
        return output_file


def main():
    analyzer = InkeiAnalyzer()
    # params = analyzer.generate_random_params()
    params = {
        'length': 137,
        'girth': 84,
        'curve': -18,
        'angle': 22,
        'glans_angle': 0,
        'shaft_exp': 87,
        'glans_exp': 124,
        'ball_dia': 37,
        'ball_hang': 45,
        'color': 'FF3737',
        'name': 'WRI',
        'subject_id': '10444075',
        'rank': 'C',
        'class': 'STANDARD MODEL',
        'stamina': 99,
        'score': 55.1,
        'notes': ['THIN'],
        'volume': 76.92,
        'ball_vol': 53.04,
        'weight': 129.97,
        'cum_ml': 12.15,
        'density': 98
    }
    
    print(f"\nParameters:")
    for k, v in params.items():
        print(f"  {k}: {v}")
    print()
    
    analyzer.generate_static_image(params, output_file=f"inkei_{params['name']}_static.png")
    
    analyzer.create_animation(
        params, 
        output_file=f"inkei_{params['name']}_animation.gif",
        fps=25,
        duration_per_phase=2.0
    )


if __name__ == "__main__":
    main()