import open3d as o3d
import time
import random
from screeninfo import get_monitors
import open3d.visualization.gui as gui
import numpy as np
import cv2

class MainWindow:
    def __init__(self):

        self.xyz_files = self.file_list()

        self.first_xyz = 0
        self.xyz_files[self.first_xyz][1] = 1

        self.next_xyz = self.first_xyz

        self.xyz_count = 1

        self.end_files_count = 0

        material = o3d.visualization.rendering.Material()


        self.choose_time = time.time()

        self.camera_zoom = 45
        self.camera_zoom_edit = self.camera_zoom

        self.result_log = []

        self.mat = o3d.io.read_point_cloud(self.xyz_files[self.first_xyz][0].split(" ")[0], format='xyzrgb')
        self.mat2 = o3d.io.read_point_cloud(self.xyz_files[self.first_xyz][0].split(" ")[1], format='xyzrgb')

        self.w = gui.Application.instance.create_window("Comparison", get_monitors()[0].width, get_monitors()[0].height)

        self.scene1 = gui.SceneWidget()
        self.scene1.scene = o3d.visualization.rendering.Open3DScene(self.w.renderer)
        self.scene1.scene.add_geometry("Model_A", self.mat, material)
        self.scene1.setup_camera(40, self.scene1.scene.bounding_box, (0, 0, 0))
        self.scene1.set_on_mouse(self.on_mouse)
        self.scene1.set_on_key(self.on_key)

        self.scene2 = gui.SceneWidget()
        self.scene2.scene = o3d.visualization.rendering.Open3DScene(self.w.renderer)
        material = o3d.visualization.rendering.Material()
        self.scene2.scene.add_geometry("Model_B", self.mat2,material)
        self.scene2.setup_camera(40, self.scene2.scene.bounding_box, (0, 0, 0))
        self.scene2.set_on_mouse(self.on_mouse)
        self.scene2.set_on_key(self.on_key)

        self.rgb = cv2.imread("./original_old/left_pyramid_sample_0.png")
        self.rgb_o3d = o3d.geometry.Image(self.rgb)

        self.scene_bottom_left = gui.SceneWidget()
        self.scene_bottom_left.scene = o3d.visualization.rendering.Open3DScene(self.w.renderer)
        #scene_bottom_left.scene.add_geometry("Model_Bo", mat,material)
        self.scene_bottom_left.scene.set_background((1.0,1.0,1.0,1.0),self.rgb_o3d)
        self.scene_bottom_left.setup_camera(self.camera_zoom, self.scene_bottom_left.scene.bounding_box, (0, 0, 0))
        self.scene_bottom_left.set_on_mouse(self.on_mouse)
        self.scene_bottom_left.set_on_key(self.on_key)

        self.scene_bottom_right = gui.SceneWidget()
    #    scene_bottom_right.scene = o3d.visualization.gui.Button()

        #reset_button = gui.Button("Reset")
        #reset_button.set_on_clicked(_set_mouse_mode_rotate)#self.reset_button_mode)
        #w.add_child(reset_button)

        self.scene_bottom_right.scene = o3d.visualization.rendering.Open3DScene(self.w.renderer)
        self.scene_bottom_right.scene.add_geometry("Model_Bo", self.mat,material)
        self.scene_bottom_right.scene.set_background((1.0,1.0,1.0,1.0),None)
        self.scene_bottom_right.setup_camera(self.camera_zoom, self.scene_bottom_right.scene.bounding_box, (0, 0, 0))
        self.scene_bottom_right.set_on_key(self.on_key)

        #################
        self.reset_button = gui.Button("Reset")
        self.reset_button.horizontal_padding_em = 0.5
        self.reset_button.vertical_padding_em = 0
        self.reset_button.set_on_clicked(self.reset_button_mode)

        self.next_button = gui.Button(str(self.end_files_count) + "/100")
        self.next_button.horizontal_padding_em = 0.5
        self.next_button.vertical_padding_em = 0
        self.next_button.set_on_clicked(self.non_button_mode)


        self.non_button_temp_1 = gui.Button("")
        self.non_button_temp_1.horizontal_padding_em = 0.5
        self.non_button_temp_1.vertical_padding_em = 0
        self.non_button_temp_1.set_on_clicked(self.non_button_mode)

        self.non_button_temp_2 = gui.Button("")
        self.non_button_temp_2.horizontal_padding_em = 0.5
        self.non_button_temp_2.vertical_padding_em = 0
        self.non_button_temp_2.set_on_clicked(self.non_button_mode)

        self.left_choose_button = gui.Button("Choose left")
        self.left_choose_button.horizontal_padding_em = 0.5
        self.left_choose_button.vertical_padding_em = 0
        self.left_choose_button.set_on_clicked(self.left_choice_button_mode)

        self.right_choose_button = gui.Button("Choose right")
        self.right_choose_button.horizontal_padding_em = 0.5
        self.right_choose_button.vertical_padding_em = 0
        self.right_choose_button.set_on_clicked(self.right_choice_button_mode)


        self.non_button_temp_3 = gui.Button("")
        self.non_button_temp_3.horizontal_padding_em = 0.5
        self.non_button_temp_3.vertical_padding_em = 0
        self.non_button_temp_3.set_on_clicked(self.non_button_mode)

        self.non_button_temp_4 = gui.Button("")
        self.non_button_temp_4.horizontal_padding_em = 0.5
        self.non_button_temp_4.vertical_padding_em = 0
        self.non_button_temp_4.set_on_clicked(self.non_button_mode)

        self.rotate_left_button = gui.Button("Rotate Left")
        self.rotate_left_button.horizontal_padding_em = 0.5
        self.rotate_left_button.vertical_padding_em = 0
        self.rotate_left_button.set_on_clicked(self.rotate_left_button_mode)


        self.rotate_right_button = gui.Button("Rotate Right")
        self.rotate_right_button.horizontal_padding_em = 0.5
        self.rotate_right_button.vertical_padding_em = 0
        self.rotate_right_button.set_on_clicked(self.rotate_right_button_mode)

        self.rotate_up_button = gui.Button("Rotate Up")
        self.rotate_up_button.horizontal_padding_em = 0.5
        self.rotate_up_button.vertical_padding_em = 0
        self.rotate_up_button.set_on_clicked(self.rotate_up_button_mode)


        self.rotate_down_button = gui.Button("Rotate Down")
        self.rotate_down_button.horizontal_padding_em = 0.5
        self.rotate_down_button.vertical_padding_em = 0
        self.rotate_down_button.set_on_clicked(self.rotate_down_button_mode)

        self.non_button_temp_5 = gui.Button("")
        self.non_button_temp_5.horizontal_padding_em = 0.5
        self.non_button_temp_5.vertical_padding_em = 0
        self.non_button_temp_5.set_on_clicked(self.non_button_mode)

        self.non_button_temp_6 = gui.Button("")
        self.non_button_temp_6.horizontal_padding_em = 0.5
        self.non_button_temp_6.vertical_padding_em = 0
        self.non_button_temp_6.set_on_clicked(self.non_button_mode)

        self.zoom_in_button = gui.Button("Zoom In")
        self.zoom_in_button.horizontal_padding_em = 0.5
        self.zoom_in_button.vertical_padding_em = 0
        self.zoom_in_button.set_on_clicked(self.zoom_in_button_mode)


        self.zoom_out_button = gui.Button("Zoom Out")
        self.zoom_out_button.horizontal_padding_em = 0.5
        self.zoom_out_button.vertical_padding_em = 0
        self.zoom_out_button.set_on_clicked(self.zoom_out_button_mode)


        self.non_button_temp_7 = gui.Button("")
        self.non_button_temp_7.horizontal_padding_em = 0.5
        self.non_button_temp_7.vertical_padding_em = 0
        self.non_button_temp_7.set_on_clicked(self.non_button_mode)

        self.non_button_temp_8 = gui.Button("")
        self.non_button_temp_8.horizontal_padding_em = 0.5
        self.non_button_temp_8.vertical_padding_em = 0
        self.non_button_temp_8.set_on_clicked(self.non_button_mode)

        self.non_button5 = gui.Button("")
        self.non_button5.horizontal_padding_em = 0.5
        self.non_button5.vertical_padding_em = 0
        self.non_button5.set_on_clicked(self.non_button_mode)

        self.Quit_button = gui.Button("")
        self.Quit_button.horizontal_padding_em = 0.5
        self.Quit_button.vertical_padding_em = 0
        self.Quit_button.set_on_clicked(self.non_button_mode)


        self.h = gui.VGrid(2)
        self.h.add_child(self.reset_button)
        self.h.add_child(self.next_button)
        self.h.add_child(self.non_button_temp_1)
        self.h.add_child(self.non_button_temp_2)
        self.h.add_child(self.rotate_left_button)
        self.h.add_child(self.rotate_right_button)
        self.h.add_child(self.rotate_up_button)
        self.h.add_child(self.rotate_down_button)
        self.h.add_child(self.non_button_temp_3)
        self.h.add_child(self.non_button_temp_4)
        self.h.add_child(self.zoom_in_button)
        self.h.add_child(self.zoom_out_button)
        self.h.add_child(self.non_button_temp_7)
        self.h.add_child(self.non_button_temp_8)
        self.h.add_child(self.non_button_temp_5)
        self.h.add_child(self.non_button_temp_6)
        self.h.add_child(self.non_button5)
        self.h.add_child(self.Quit_button)
        self.h.add_child(self.left_choose_button)
        self.h.add_child(self.right_choose_button)

        self.w.add_child(self.h)


        self.Flag_reset = False
        self.Flag_check = False
        #################

        self.w.add_child(self.scene1)
        self.w.add_child(self.scene2)
        self.w.add_child(self.scene_bottom_left)
        self.w.add_child(self.scene_bottom_right)

        self.w.set_on_layout(self.on_layout())

        # Start running
        #threading.Thread(name='UpdateMain', target=self.update_main).start()

    def on_key(self, e):
        if e.key == gui.KeyName.UP:
            if e.type == gui.KeyEvent.DOWN:
                R = self.mat.get_rotation_matrix_from_xyz((-np.pi / 16, 0, 0))
                self.mat.rotate(R, center=self.mat.get_center())
                self.scene1.scene.remove_geometry("Model_A")
                material = o3d.visualization.rendering.Material()

                R = self.mat2.get_rotation_matrix_from_xyz((-np.pi / 16, 0, 0))
                self.mat2.rotate(R, center=self.mat2.get_center())
                self.scene2.scene.remove_geometry("Model_B")

                self.scene1.scene.add_geometry("Model_A", self.mat, material)
                self.scene2.scene.add_geometry("Model_B", self.mat2, material)
            return gui.Widget.EventCallbackResult.HANDLED
        if e.key == gui.KeyName.DOWN:
            if e.type == gui.KeyEvent.DOWN:
                R = self.mat.get_rotation_matrix_from_xyz((np.pi / 16, 0, 0))
                self.mat.rotate(R, center=self.mat.get_center())
                self.scene1.scene.remove_geometry("Model_A")
                material = o3d.visualization.rendering.Material()

                R = self.mat2.get_rotation_matrix_from_xyz((np.pi / 16, 0, 0))
                self.mat2.rotate(R, center=self.mat2.get_center())
                self.scene2.scene.remove_geometry("Model_B")

                self.scene1.scene.add_geometry("Model_A", self.mat, material)
                self.scene2.scene.add_geometry("Model_B", self.mat2, material)
            return gui.Widget.EventCallbackResult.HANDLED
        if e.key == gui.KeyName.LEFT:
            if e.type == gui.KeyEvent.DOWN:
                R = self.mat.get_rotation_matrix_from_xyz((0, -np.pi / 16, 0))
                self.mat.rotate(R, center=self.mat.get_center())
                self.scene1.scene.remove_geometry("Model_A")
                material = o3d.visualization.rendering.Material()

                R = self.mat2.get_rotation_matrix_from_xyz((0, -np.pi / 16, 0))
                self.mat2.rotate(R, center=self.mat2.get_center())
                self.scene2.scene.remove_geometry("Model_B")

                self.scene1.scene.add_geometry("Model_A", self.mat, material)
                self.scene2.scene.add_geometry("Model_B", self.mat2, material)
            return gui.Widget.EventCallbackResult.HANDLED
        if e.key == gui.KeyName.RIGHT:
            if e.type == gui.KeyEvent.DOWN:
                R = self.mat.get_rotation_matrix_from_xyz((0, np.pi / 16, 0))
                self.mat.rotate(R, center=self.mat.get_center())
                self.scene1.scene.remove_geometry("Model_A")
                material = o3d.visualization.rendering.Material()

                R = self.mat2.get_rotation_matrix_from_xyz((0, np.pi / 16, 0))
                self.mat2.rotate(R, center=self.mat2.get_center())
                self.scene2.scene.remove_geometry("Model_B")

                self.scene1.scene.add_geometry("Model_A", self.mat, material)
                self.scene2.scene.add_geometry("Model_B", self.mat2, material)
            return gui.Widget.EventCallbackResult.HANDLED
        return gui.Widget.EventCallbackResult.IGNORED

    def on_mouse(self, e):
        if e.type == gui.MouseEvent.BUTTON_DOWN:
            return gui.Widget.EventCallbackResult.CONSUMED
        else:
            return gui.Widget.EventCallbackResult.HANDLED
        #return gui.Widget.EventCallbackResult.CONSUMED

    def on_layout(self):
        r = self.w.content_rect
        self.scene1.frame = gui.Rect(r.x, r.y, r.width / 2, r.height * 3 / 5)
        self.scene2.frame = gui.Rect(r.x + r.width / 2 + 1, r.y, r.width / 2, r.height * 3 / 5)
        self.scene_bottom_left.frame = gui.Rect(r.x,r.y + (r.height * 3 / 5) + 1, r.width/2, r.height * 2 / 5)
        self.h.frame = gui.Rect(r.x + r.width / 2 + 1, r.y + (r.height * 3 / 5) + 1, r.x + r.width / 2, r.y + r.height * 2 / 5)
    def reset_button_mode(self):
        self.reset_geometry()

    def next_button_mode(self):
        self.add_new_geometry()


    def left_choice_button_mode(self):
        if self.end_files_count != 101:
            self.end_files_count += 1
            self.next_button.text = str(self.end_files_count) + "/100"
            self.left_write()
            self.add_new_geometry()
        elif self.end_files_count == 101:
            self.f = open("Final_result.txt", 'a')
            for i in range(len(self.result_log)):
                self.f.write(self.result_log[i])
            self.f.close()

            gui.Application.instance.quit()

    def right_choice_button_mode(self):
        if self.end_files_count != 101:
            self.end_files_count += 1
            self.next_button.text = str(self.end_files_count) + "/100"
            self.right_write()
            self.add_new_geometry()
        elif self.end_files_count == 101:
            self.f = open("Final_result.txt", 'a')
            for i in range(len(self.result_log)):
                self.f.write(self.result_log[i])
            self.f.close()

            gui.Application.instance.quit()

    def non_button_mode(self):
        None

    def rotate_up_button_mode(self):
        R = self.mat.get_rotation_matrix_from_xyz((-np.pi / 16, 0, 0))
        self.mat.rotate(R, center=self.mat.get_center())
        self.scene1.scene.remove_geometry("Model_A")
        material = o3d.visualization.rendering.Material()

        R = self.mat2.get_rotation_matrix_from_xyz((-np.pi / 16, 0, 0))
        self.mat2.rotate(R, center=self.mat2.get_center())
        self.scene2.scene.remove_geometry("Model_B")

        self.scene1.scene.add_geometry("Model_A", self.mat, material)
        self.scene2.scene.add_geometry("Model_B", self.mat2, material)

    def rotate_down_button_mode(self):
        R = self.mat.get_rotation_matrix_from_xyz((np.pi / 16, 0, 0))
        self.mat.rotate(R, center=self.mat.get_center())
        self.scene1.scene.remove_geometry("Model_A")
        material = o3d.visualization.rendering.Material()

        R = self.mat2.get_rotation_matrix_from_xyz((np.pi / 16, 0, 0))
        self.mat2.rotate(R, center=self.mat2.get_center())
        self.scene2.scene.remove_geometry("Model_B")

        self.scene1.scene.add_geometry("Model_A", self.mat, material)
        self.scene2.scene.add_geometry("Model_B", self.mat2, material)

    def rotate_left_button_mode(self):
        R = self.mat.get_rotation_matrix_from_xyz((0, -np.pi / 16, 0))
        self.mat.rotate(R, center=self.mat.get_center())
        self.scene1.scene.remove_geometry("Model_A")
        material = o3d.visualization.rendering.Material()

        R = self.mat2.get_rotation_matrix_from_xyz((0, -np.pi / 16, 0))
        self.mat2.rotate(R, center=self.mat2.get_center())
        self.scene2.scene.remove_geometry("Model_B")

        self.scene1.scene.add_geometry("Model_A", self.mat, material)
        self.scene2.scene.add_geometry("Model_B", self.mat2, material)

    def rotate_right_button_mode(self):
        R = self.mat.get_rotation_matrix_from_xyz((0, np.pi / 16, 0))
        self.mat.rotate(R, center=self.mat.get_center())
        self.scene1.scene.remove_geometry("Model_A")
        material = o3d.visualization.rendering.Material()

        R = self.mat2.get_rotation_matrix_from_xyz((0, np.pi / 16, 0))
        self.mat2.rotate(R, center=self.mat2.get_center())
        self.scene2.scene.remove_geometry("Model_B")

        self.scene1.scene.add_geometry("Model_A", self.mat, material)
        self.scene2.scene.add_geometry("Model_B", self.mat2, material)

    def zoom_in_button_mode(self):
        material = o3d.visualization.rendering.Material()

        self.scene1.scene.remove_geometry("Model_A")
        self.scene2.scene.remove_geometry("Model_B")

        self.camera_zoom_edit -= 5

        self.scene1.setup_camera(self.camera_zoom_edit, self.scene1.scene.bounding_box, (0, 0, 0))
        self.scene2.setup_camera(self.camera_zoom_edit, self.scene2.scene.bounding_box, (0, 0, 0))


        self.scene1.scene.add_geometry("Model_A", self.mat, material)
        self.scene2.scene.add_geometry("Model_B", self.mat2, material)

    def zoom_out_button_mode(self):
        material = o3d.visualization.rendering.Material()

        self.scene1.scene.remove_geometry("Model_A")
        self.scene2.scene.remove_geometry("Model_B")

        self.camera_zoom_edit += 5

        self.scene1.setup_camera(self.camera_zoom_edit, self.scene1.scene.bounding_box, (0, 0, 0))
        self.scene2.setup_camera(self.camera_zoom_edit, self.scene2.scene.bounding_box, (0, 0, 0))

        self.scene1.scene.add_geometry("Model_A", self.mat, material)
        self.scene2.scene.add_geometry("Model_B", self.mat2, material)

    def Quit_button_mode(self):
        self.f = open("Final_result.txt", 'a')
        for i in range(len(self.result_log)):
            self.f.write(self.result_log[i])
        self.f.close()

        gui.Application.instance.quit()


    def reset_geometry(self):
        self.scene1.scene.remove_geometry("Model_A")
        self.scene2.scene.remove_geometry("Model_B")
        material = o3d.visualization.rendering.Material()

        if self.xyz_files[self.next_xyz][2] == 1:
            self.mat = o3d.io.read_point_cloud(self.xyz_files[self.next_xyz][0].split(" ")[1], format='xyzrgb')
            self.mat2 = o3d.io.read_point_cloud(self.xyz_files[self.next_xyz][0].split(" ")[0], format='xyzrgb')
        else:
            self.mat = o3d.io.read_point_cloud(self.xyz_files[self.next_xyz][0].split(" ")[0], format='xyzrgb')
            self.mat2 = o3d.io.read_point_cloud(self.xyz_files[self.next_xyz][0].split(" ")[1], format='xyzrgb')

        self.scene1.scene.add_geometry("Model_A", self.mat, material)
        self.scene2.scene.add_geometry("Model_B", self.mat2,material)
        self.camera_zoom_edit = 40
        self.scene1.setup_camera(self.camera_zoom_edit, self.scene1.scene.bounding_box, (0, 0, 0))
        self.scene2.setup_camera(self.camera_zoom_edit, self.scene2.scene.bounding_box, (0, 0, 0))

        self.rgb2 = cv2.imread("./original_old/" + self.xyz_files[self.next_xyz][0].split(" ")[2] + ".png")
        self.rgb_o3d2 = o3d.geometry.Image(self.rgb2)
        self.scene_bottom_left.scene.set_background((1.0,1.0,1.0,1.0),self.rgb_o3d2)

    def add_new_geometry(self):
        self.scene1.scene.remove_geometry("Model_A")
        self.scene2.scene.remove_geometry("Model_B")
        material = o3d.visualization.rendering.Material()

        while self.xyz_count != len(self.xyz_files):
            next_xyz = random.randint(0,len(self.xyz_files)-1)
            if self.xyz_files[next_xyz][1] == 0:
                self.xyz_count += 1
                self.xyz_files[next_xyz][1] = 1
                self.next_xyz = next_xyz
                break

        if self.xyz_count != len(self.xyz_files):

            if random.randint(0,9) > 4:
                self.mat = o3d.io.read_point_cloud(self.xyz_files[self.next_xyz][0].split(" ")[0], format='xyzrgb')
                self.mat2 = o3d.io.read_point_cloud(self.xyz_files[self.next_xyz][0].split(" ")[1], format='xyzrgb')
                self.xyz_files[self.next_xyz][2] = 0
            else:
                self.mat = o3d.io.read_point_cloud(self.xyz_files[self.next_xyz][0].split(" ")[1], format='xyzrgb')
                self.mat2 = o3d.io.read_point_cloud(self.xyz_files[self.next_xyz][0].split(" ")[0], format='xyzrgb')
                self.xyz_files[self.next_xyz][2] = 1

            self.camera_zoom_edit = 40

            self.scene1.scene.add_geometry("Model_A", self.mat, material)
            self.scene2.scene.add_geometry("Model_B", self.mat2,material)
            self.scene1.setup_camera(self.camera_zoom_edit, self.scene1.scene.bounding_box, (0, 0, 0))
            self.scene2.setup_camera(self.camera_zoom_edit, self.scene2.scene.bounding_box, (0, 0, 0))

            self.rgb2 = cv2.imread("./original_old/" + self.xyz_files[self.next_xyz][0].split(" ")[2] + ".png")

            self.rgb_o3d2 = o3d.geometry.Image(self.rgb2)
            self.scene_bottom_left.scene.set_background((1.0,1.0,1.0,1.0),self.rgb_o3d2)

    def left_write(self):
        if self.xyz_files[self.next_xyz][2] == 1:
            model_A_name = self.xyz_files[self.next_xyz][0].split(" ")[1].split("/")[-2]
            model_B_name = self.xyz_files[self.next_xyz][0].split(" ")[0].split("/")[-2]
        else:
            model_A_name = self.xyz_files[self.next_xyz][0].split(" ")[0].split("/")[-2]
            model_B_name = self.xyz_files[self.next_xyz][0].split(" ")[1].split("/")[-2]

        image_name = self.xyz_files[self.next_xyz][0].split(" ")[2]

        self.choose_time_result = (time.time() - self.choose_time)
        self.choose_time = time.time()

        txt_write_line = model_A_name + "\t" + model_B_name + "\t" + image_name + "\t" + "choise" + "\t" + model_A_name + "\t" + str(self.choose_time_result) + '\n'
        #print(txt_write_line)
        self.result_log.append(txt_write_line)

        self.f = open("result.txt", 'a')
        self.f.write(txt_write_line)
        self.f.close()

    def right_write(self):
        if self.xyz_files[self.next_xyz][2] == 1:
            model_A_name = self.xyz_files[self.next_xyz][0].split(" ")[1].split("/")[-2]
            model_B_name = self.xyz_files[self.next_xyz][0].split(" ")[0].split("/")[-2]
        else:
            model_A_name = self.xyz_files[self.next_xyz][0].split(" ")[0].split("/")[-2]
            model_B_name = self.xyz_files[self.next_xyz][0].split(" ")[1].split("/")[-2]

        image_name = self.xyz_files[self.next_xyz][0].split(" ")[2]

        self.choose_time_result = (time.time() - self.choose_time)
        self.choose_time = time.time()

        txt_write_line = model_A_name + "\t" + model_B_name + "\t" + image_name + "\t" + "choise" + "\t" + model_B_name + "\t" + str(self.choose_time_result) + '\n'
        #print(txt_write_line)

        self.result_log.append(txt_write_line)

        self.f = open("result.txt", 'a')
        self.f.write(txt_write_line)
        self.f.close()

    def file_list(self):
        xyz_files = []
        f = open("./old_xyz/xyz_list.txt","r")
        files = f.readlines()
        for file in files:
            xyz_files.append([file.strip(), 0, 0])
        f.close()
        return xyz_files

def main():

    gui.Application.instance.initialize()

    W = MainWindow()

    gui.Application.instance.run()

if __name__ == "__main__":
    main()