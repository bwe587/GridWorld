import pyglet
import os
import tkinter as tk
import numpy as np
import time
import random
import webbrowser
from pathlib import Path

pyglet.options['win32_gdi_font'] = True

pyglet.font.add_file('digital.ttf')

#window.wm_attributes('-fullscreen', 'True')

class GridWorld:

	def __init__(self, APP):

		self.tile_colors = {"White": "#ffffff",
							"Gray": "#d8dee9", 
							"Blue": "#5e81ac", 
							"Green": "#a3be8c"}

		self.actions = ("LEFT","DOWN","RIGHT","UP")

		self.agent = tk.PhotoImage(file="Resources/Sprites/Drone_Loris.png")
		self.ASSETS_PATH = Path(r"Resources/GUI")
		self.reward = 0
		self.createWindow()
		self.createGUI()

	def createWindow(self):

		self.canvas = tk.Canvas(APP,
								height = 1024,
								width = 1280,
								highlightthickness = 0)

		self.canvas.place(x=0,
					 	  y=0)

		self.canvas.create_rectangle(0.0,
									 0.0,
									 1280.0,
									 1024.0,
									 fill="#2E3440")

	def createGUI(self):
	
		self.LHSHeader()
		self.Header()
		self.RHSHeader()
		self.RHSPanel()
		self.RHSFooter()
		self.Footer()
		self.LHSFooter()
		self.LHSPanel()
		self.Screws()
		self.TextWorld()
		self.LogoRobot()
		self.TextGrid()
		self.TextGamma()
		self.TextSteps()
		self.TextExplr()
		self.TextPlaceAgent()
		self.TextCreateGrid()
		self.BtnInfo()
		self.BtnGitHub()
		self.BtnQuit()
		self.BtnIncreaseGridCol()
		self.BtnDecreaseGridCol()
		self.ValCol()
		self.BtnIncreaseGridRow()
		self.BtnDecreaseGridRow()
		self.ValRow()
		self.BtnCreateGrid()
		self.BtnIncreaseXCoord()
		self.BtnDecreaseXCoord()
		self.ValCoordX()
		self.BtnIncreaseYCoord()
		self.BtnDecreaseYCoord()
		self.ValCoordY()
		self.BtnPlaceAgent()
		self.BtnIncreaseGamma()
		self.BtnDecreaseGamma()
		self.ValGamma()
		self.BtnIncreaseSteps()
		self.BtnDecreaseSteps()
		self.ValSteps()
		self.BtnIncreaseExplr()
		self.BtnDecreaseExplr()
		self.ValExplr()
		self.BtnStop()
		self.BtnStart()
		
	def Header(self):

		self.img_header = tk.PhotoImage(file=self.relative_to_assets("header.png"))

		self.header = self.canvas.create_image(471.0, 
											   57.0, 
											   image=self.img_header)

	def LogoRobot(self):

		self.img_logo_robot = tk.PhotoImage(file=self.relative_to_assets("robot_logo.png"))

		self.robot_logo = self.canvas.create_image(649.0,
										 		   57.0,
												   image=self.img_logo_robot)

	def RHSPanel(self):

		self.img_rhs_panel = tk.PhotoImage(file=self.relative_to_assets("right_frame.png"))

		self.rhs_panel = self.canvas.create_image(1074.0,
												  514.0,
												  image=self.img_rhs_panel)

	def LHSPanel(self):

		self.img_lhs_panel = tk.PhotoImage(file=self.relative_to_assets("left_frame.png"))

		self.lhs_panel = self.canvas.create_image(39.0,
												  514.0,
												  image=self.img_lhs_panel)

	def Footer(self):

		self.img_footer = tk.PhotoImage(file=self.relative_to_assets("footer.png"))

		self.footer = self.canvas.create_image(471.0,
											   969.0,
											   image=self.img_footer)

	def LHSHeader(self):

		self.img_lhs_header = tk.PhotoImage(file=self.relative_to_assets("left_frame_header.png"))

		self.lhs_header = self.canvas.create_image(33.0,
												   57.0,
												   image=self.img_lhs_header)

	def LHSFooter(self):

		self.img_lhs_footer = tk.PhotoImage(file=self.relative_to_assets("left_frame_footer.png"))

		self.lhs_footer = self.canvas.create_image(33.0,
												   969.0,
												   image=self.img_lhs_footer)

	def RHSHeader(self):

		self.img_rhs_header = tk.PhotoImage(file=self.relative_to_assets("right_frame_header.png"))

		self.rhs_header = self.canvas.create_image(1078.0,
												   57.0,
												   image=self.img_rhs_header)

	def RHSFooter(self):

		self.img_rhs_footer = tk.PhotoImage(file=self.relative_to_assets("right_frame_footer.png"))

		self.rhs_footer = self.canvas.create_image(1078.0,
												   969.0,
												   image=self.img_rhs_footer)

	def Screws(self):

		self.img_screw_1 = tk.PhotoImage(file=self.relative_to_assets("screw_1.png"))

		self.screw_1 = self.canvas.create_image(33.5,
												53.0,
												image=self.img_screw_1)

		self.img_screw_2 = tk.PhotoImage(file=self.relative_to_assets("screw_2.png"))

		self.screw_2 = self.canvas.create_image(33.5,
												969.0,
												image=self.img_screw_2)

		self.img_screw_3 = tk.PhotoImage(file=self.relative_to_assets("screw_3.png"))

		self.screw_3 = self.canvas.create_image(1240.5,
												53.0,
												image=self.img_screw_3)

		self.img_screw_4 = tk.PhotoImage(file=self.relative_to_assets("screw_4.png"))

		self.screw_4 = self.canvas.create_image(1240.5,
												969.0,
												image=self.img_screw_4)

		self.img_screw_5 = tk.PhotoImage(file=self.relative_to_assets("screw_5.png"))

		self.screw_5  = self.canvas.create_image(912.5,
												 53.0,
												 image=self.img_screw_5)

		self.img_screw_6 = tk.PhotoImage(file=self.relative_to_assets("screw_6.png"))

		self.screw_6 = self.canvas.create_image(912.5,
												969.0,
												image=self.img_screw_6)

	def TextWorld(self):

		self.img_txt_world = tk.PhotoImage(file=self.relative_to_assets("text_world.png"))

		self.txt_world = self.canvas.create_image(775.2001953125,
												  53.9609375,
												  image=self.img_txt_world)

	def TextGrid(self):

		self.img_txt_grid = tk.PhotoImage(file=self.relative_to_assets("text_grid.png"))

		self.txt_grid = self.canvas.create_image(530.22412109375,
												 52.703125,
												 image=self.img_txt_grid)

	def BtnIncreaseGridCol(self):

		self.img_btn_inc_grid_col = tk.PhotoImage(file=self.relative_to_assets("button_inc_grid_col.png"))

		self.btn_inc_grid_col = tk.Button(image=self.img_btn_inc_grid_col,
										  borderwidth=0,
										  bg = '#434c5e',
										  activebackground='#434c5e',
										  highlightthickness=0,
										  command=self.increaseDimCol,
										  relief="flat")

		self.btn_inc_grid_col.place(x=889.69970703125,
								    y=156.408203125,
								    width=70.6005859375,
								    height=68.841796875)

	def BtnDecreaseGridCol(self):

		self.img_btn_dec_grid_col = tk.PhotoImage(file=self.relative_to_assets("button_dec_grid_col.png"))

		self.btn_dec_grid_col = tk.Button(image=self.img_btn_dec_grid_col,
										  borderwidth=0,
										  bg = '#434c5e',
										  activebackground='#434c5e',
										  highlightthickness=0,
										  command=self.decreaseDimCol,
										  relief="flat")

		self.btn_dec_grid_col.place(x=888.876953125,
								    y=259.75,
								    width=71.24609375,
								    height=69.083984375)

	def BtnIncreaseGridRow(self):

		self.img_btn_inc_grid_row = tk.PhotoImage(file=self.relative_to_assets("button_inc_grid_row.png"))

		self.btn_inc_grid_row = tk.Button(image=self.img_btn_inc_grid_row,
										  borderwidth=0,
										  bg = '#434c5e',
										  activebackground='#434c5e',
										  highlightthickness=0,
										  command=self.increaseDimRow,
										  relief="flat")

		self.btn_inc_grid_row.place(x=1185.69970703125,
									y=156.408203125,
									width=70.6005859375,
									height=68.841796875)

	def BtnDecreaseGridRow(self):

		self.img_btn_dec_grid_row = tk.PhotoImage(file=self.relative_to_assets("button_dec_grid_row.png"))

		self.btn_dec_grid_row = tk.Button(image=self.img_btn_dec_grid_row,
										  borderwidth=0,
										  bg = '#434c5e',
										  activebackground='#434c5e',
										  highlightthickness=0,
										  command=self.decreaseDimRow,
										  relief="flat")

		self.btn_dec_grid_row.place(x=1184.876953125,
								    y=259.75,
								    width=71.24609375,
								    height=69.083984375)

	def BtnIncreaseGamma(self):

		self.button_image_increase_gamma = tk.PhotoImage(file=self.relative_to_assets("button_inc_gamma.png"))

		self.button_increase_gamma = tk.Button(image=self.button_image_increase_gamma,
											   borderwidth=0,
											   bg = '#434c5e',
											   activebackground='#434c5e',
											   highlightthickness=0,
											   command=lambda: self.increaseGamma(),
											   relief="flat")

		self.button_increase_gamma.place(x=947.0,
									     y=743.1484375,
									     width=24.67138671875,
									     height=24.705078125)

	def BtnDecreaseGamma(self):

		self.button_image_decrease_gamma = tk.PhotoImage(file=self.relative_to_assets("button_dec_gamma.png"))

		self.button_decrease_gamma = tk.Button(image=self.button_image_decrease_gamma,
											   borderwidth=0,
											   bg = '#434c5e',
											   activebackground='#434c5e',
											   highlightthickness=0,
											   command=lambda: self.decreaseGamma(),
											   relief="flat")

		self.button_decrease_gamma.place(x=895.32861328125,
									     y=743.1484375,
									     width=24.67138671875,
									     height=24.705078125)

	def BtnIncreaseExplr(self):

		self.button_image_increase_explr = tk.PhotoImage(file=self.relative_to_assets("button_inc_explr.png"))

		self.button_increase_explr = tk.Button(image=self.button_image_increase_explr,
											   borderwidth=0,
											   bg = '#434c5e',
											   activebackground='#434c5e',
											   highlightthickness=0,
											   command=lambda: self.increaseExplr(),
											   relief="flat")

		self.button_increase_explr.place(x=1223.0,
									     y=743.1484375,
									     width=24.67138671875,
									     height=24.705078125)

	def BtnDecreaseExplr(self):

		self.button_image_decrease_explr = tk.PhotoImage(file=self.relative_to_assets("button_dec_explr.png"))

		self.button_decrease_explr = tk.Button(image=self.button_image_decrease_explr,
											   borderwidth=0,
											   bg = '#434c5e',
											   activebackground='#434c5e',
											   highlightthickness=0,
											   command=lambda: self.decreaseExplr(),
											   relief="flat")

		self.button_decrease_explr.place(x=1175.32861328125,
									     y=743.1484375,
									     width=24.67138671875,
									     height=24.705078125)

	def BtnIncreaseSteps(self):

		self.button_image_increase_steps = tk.PhotoImage(file=self.relative_to_assets("button_inc_step.png"))

		self.button_increase_steps = tk.Button(image=self.button_image_increase_steps,
											   borderwidth=0,
											   bg = '#434c5e',
											   activebackground='#434c5e',
											   highlightthickness=0,
											   command=lambda: self.increaseSteps(),
											   relief="flat")

		self.button_increase_steps.place(x=1113.0,
									     y=743.1484375,
									     width=24.67138671875,
									     height=24.705078125)

	def BtnDecreaseSteps(self):

		self.button_image_decrease_steps = tk.PhotoImage(file=self.relative_to_assets("button_dec_step.png"))

		self.button_decrease_steps = tk.Button(image=self.button_image_decrease_steps,
											   borderwidth=0,
											   bg = '#434c5e',
											   activebackground='#434c5e',
											   highlightthickness=0,
											   command=lambda: self.decreaseSteps(),
											   relief="flat")

		self.button_decrease_steps.place(x=1011.32861328125,
										 y=743.1484375,
										 width=24.67138671875,
										 height=24.705078125)

	def BtnCreateGrid(self):

		self.button_image_create_grid = tk.PhotoImage(file=self.relative_to_assets("create_grid_button.png"))

		self.button_create_grid = tk.Button(image=self.button_image_create_grid,
											borderwidth=0,
											bg = '#434c5e',
											activebackground='#434c5e',
											highlightthickness=0,
											command=self.createGrid, 
											relief="flat")

		self.button_create_grid.place(x=989.90673828125,
									  y=297.779296875,
									  width=167.1865234375,
									  height=63.869140625)

	def ValCol(self):

		self.img_val_col = tk.PhotoImage(file=self.relative_to_assets("entry_1.png"))

		self.img_val_col_place = self.canvas.create_image(1033.0,
										 240.0,
										 image=self.img_val_col)

		self.val_col = tk.Label(bd=0,
							    bg="#EBEFF4",
							    justify='center',
							    font=('Digital-7',24),
							    text="1",
							    highlightthickness=0)

		self.val_col.place(x=1007.5,
					  	   y=220.0,
						   width=50.0,
						   height=40.0)

	def ValRow(self):

		self.img_val_row = tk.PhotoImage(file=self.relative_to_assets("entry_2.png"))

		self.img_val_row_place = self.canvas.create_image(1111.0,
										 		   		  240.0,
										 		   		  image=self.img_val_row)

		self.val_row = tk.Label(bd=0,
								bg="#EBEFF4",
								justify='center',
								font=('Digital-7',24),
								text="1",
								highlightthickness=0)

		self.val_row.place(x=1087.0,
						   y=220.0,
						   width=50.0,
						   height=40.0)

	def ValGamma(self):

		self.img_val_gamma = tk.PhotoImage(file=self.relative_to_assets("entry_3.png"))

		self.img_val_gamma_place = self.canvas.create_image(932.0,
										 702.0,
										 image=self.img_val_gamma)

		self.val_gamma = tk.Label(bd=0,
						bg="#EBEFF4",
						justify='center',
						font=('Digital-7',24),
						text="0.01",
						highlightthickness=0)

		self.val_gamma.place(x=907.5,
							 y=682.5,
							 width=50.0,
							 height=40.0)

	def ValSteps(self):

		self.img_val_steps = tk.PhotoImage(file=self.relative_to_assets("entry_4.png"))

		self.img_val_steps_place = self.canvas.create_image(1074.0,
															702.0,
															image=self.img_val_steps)

		self.val_steps = tk.Label(bd=0,
								  bg="#EBEFF4",
								  fg="#000716",
								  justify='center',
								  font=('Digital-7',24),
								  text="1000",
								  highlightthickness=0)

		self.val_steps.place(x=1000.0,
						     y=682.5,
						     width=147.5,
						     height=40.0)

	def ValExplr(self):

		self.img_val_explr = tk.PhotoImage(file=self.relative_to_assets("entry_5.png"))

		self.img_val_explr_place = self.canvas.create_image(1212.0,
															702.0,
															image=self.img_val_explr)

		self.val_explr = tk.Label(bd=0,
								  bg="#EBEFF4",
								  fg="#000716",
								  justify='center',
								  font=('Digital-7',24),
								  text=".2",
								  highlightthickness=0)

		self.val_explr.place(x=1187.5,
							 y=682.5,
							 width=50.0,
							 height=40.0)

	def BtnInfo(self):

		self.button_image_info = tk.PhotoImage(file=self.relative_to_assets("info_button.png"))

		self.button_info = tk.Button(image=self.button_image_info,
									 borderwidth=0,
									 highlightthickness=0,
									 bg='#434c5e',
									 activebackground='#434c5e',
									 command=lambda: self.call_popup(APP),
									 relief="flat")

		self.button_info.place(x=71.0,
							   y=932.0,
							   width=83.01513671875,
							   height=83.099609375)

	def BtnQuit(self):

		self.button_image_exit = tk.PhotoImage(file=self.relative_to_assets("exit_button.png"))

		self.button_exit = tk.Button(image=self.button_image_exit,
									 borderwidth=0,
									 highlightthickness=0,
									 bg='#434c5e',
									 activebackground='#434c5e',
									 command=lambda: APP.quit(),
									 relief="flat")

		self.button_exit.place(x=775.0,
							   y=932.0,
							   width=82.0,
							   height=82.0)

	def BtnGitHub(self):

		self.button_image_github = tk.PhotoImage(file=self.relative_to_assets("github_button.png"))

		self.button_github = tk.Button(image=self.button_image_github,
									   borderwidth=0,
									   highlightthickness=0,
									   bg='#434c5e',
									   activebackground='#434c5e',
									   command=lambda: webbrowser.open_new("https://github.com/bwe587/GridWorld"),
									   relief="flat")

		self.button_github.place(x=436.0,
								 y=932.0,
								 width=80.0,
								 height=80.0)

	def TextGamma(self):

		self.image_text_gamma = tk.PhotoImage(file=self.relative_to_assets("text_gamma.png"))

		self.text_gamma = self.canvas.create_image(927.13525390625,
												   639.240234375,
												   image=self.image_text_gamma)

	def TextSteps(self):

		self.image_text_steps = tk.PhotoImage(file=self.relative_to_assets("text_steps.png"))

		self.text_steps = self.canvas.create_image(1072.75146484375,
												   641.216796875,
												   image=self.image_text_steps)

	def TextExplr(self):

		self.image_text_explr = tk.PhotoImage(file=self.relative_to_assets("text_explr.png"))

		self.text_explr = self.canvas.create_image(1214.42333984375, 
									   			   640.48046875,
									   			   image=self.image_text_explr)

	def TextCreateGrid(self):

		self.image_text_create_grid = tk.PhotoImage(file=self.relative_to_assets("text_create_grid.png"))

		self.text_create_grid = self.canvas.create_image(1072.96337890625,
														 173.3515625,
											 			 image=self.image_text_create_grid)

	def BtnIncreaseXCoord(self):

		self.button_image_12 = tk.PhotoImage(file=self.relative_to_assets("button_inc_xcoord.png"))

		self.btn_increase_coord_x = tk.Button(image=self.button_image_12,
											  borderwidth=0,
											  bg = '#434c5e',
											  activebackground='#434c5e',
											  highlightthickness=0,
											  command= self.increaseCoordX,
											  relief="flat")

		self.btn_increase_coord_x.place(x=889.69970703125,
										y=398.408203125,
										width=70.6005859375,
										height=68.841796875)

	def BtnDecreaseXCoord(self):

		self.button_image_13 = tk.PhotoImage(file=self.relative_to_assets("button_dec_xcoord.png"))

		self.btn_decrease_coord_x = tk.Button(image=self.button_image_13,
											  borderwidth=0,
											  bg = '#434c5e',
											  activebackground='#434c5e',
											  highlightthickness=0,
											  command=self.decreaseCoordX,
											  relief="flat")

		self.btn_decrease_coord_x.place(x=888.876953125,
										y=501.75,
										width=71.24609375,
										height=69.083984375)

	def BtnIncreaseYCoord(self):

		self.button_image_14 = tk.PhotoImage(file=self.relative_to_assets("button_inc_ycoord.png"))

		self.btn_increase_coord_y = tk.Button(image=self.button_image_14,
											  borderwidth=0,
											  bg = '#434c5e',
											  activebackground='#434c5e',
											  highlightthickness=0,
											  command=self.increaseCoordY,
											  relief="flat")

		self.btn_increase_coord_y.place(x=1185.69970703125,
										y=398.408203125,
										width=70.6005859375,
										height=68.841796875)

	def BtnDecreaseYCoord(self):

		self.button_image_15 = tk.PhotoImage(file=self.relative_to_assets("button_dec_ycoord.png"))

		self.btn_decrease_coord_y = tk.Button(image=self.button_image_15,
											  borderwidth=0,
											  bg = '#434c5e',
											  activebackground='#434c5e',
											  highlightthickness=0,
											  command= self.decreaseCoordY,
											  relief="flat")

		self.btn_decrease_coord_y.place(x=1184.876953125,
										y=501.75,
										width=71.24609375,
										height=69.083984375)

	def BtnStart(self):

		self.button_image_start = tk.PhotoImage(file=self.relative_to_assets("start_button.png"))

		self.button_start = tk.Button(image=self.button_image_start,
									  borderwidth=0,
									  bg = '#434c5e',
									  activebackground='#434c5e',
									  highlightthickness=0,
									  command=lambda: self.runIterations(),
									  relief="flat")

		self.button_start.place(x=1108.25,
								y=801.333984375,
								width=111.74951171875,
								height=80.333984375)
				
	def BtnPlaceAgent(self):

		self.button_image_place_agent = tk.PhotoImage(file=self.relative_to_assets("place_agent_button.png"))

		self.button_place_agent = tk.Button(image=self.button_image_place_agent,
										    borderwidth=0,
										    bg = '#434c5e',
										    activebackground='#434c5e',
										    highlightthickness=0,
										    command=self.initAgent,
										    relief="flat")

		self.button_place_agent.place(x=989.90673828125,
									  y=539.779296875,
									  width=167.1865234375,
									  height=63.869140625)

	def ValCoordX(self):

		self.img_val_x = tk.PhotoImage(file=self.relative_to_assets("entry_6.png"))

		self.img_val_x_place = self.canvas.create_image(1033.0,
														482.0,
														image=self.img_val_x)

		self.val_x = tk.Label(bd=0,
							  bg="#EBEFF4",
							  justify='center',
							  font=('Digital-7',24),
							  text="1",
							  highlightthickness=0)

		self.val_x.place(x=1007.5,
					     y=462.5,
					     width=50.0,
					     height=40.0)

	def ValCoordY(self):

		self.img_val_y = tk.PhotoImage(file=self.relative_to_assets("entry_7.png"))

		self.img_val_y.place = self.canvas.create_image(1111.0,
										 482.0,
										 image=self.img_val_y)

		self.val_y = tk.Label(bd=0,
							 bg="#EBEFF4",
							 fg="#000716",
							 justify='center',
							 font=('Digital-7',24),
							 text="1",
							 highlightthickness=0)

		self.val_y.place(x=1087.0,
						 y=462.5,
						 width=50.0,
						 height=40.0)

	def TextPlaceAgent(self):

		self.image_text_place_agent = tk.PhotoImage(file=self.relative_to_assets("text_place_agent.png"))

		self.text_place_agent = self.canvas.create_image(1074.0595703125,
												   		 417.48046875,
												   		 image=self.image_text_place_agent)

	def BtnStop(self):

		self.button_image_stop = tk.PhotoImage(file=self.relative_to_assets("stop_button.png"))

		self.button_stop = tk.Button(image=self.button_image_stop,
						   borderwidth=0,
						   bg = '#434c5e',
						   activebackground='#434c5e',
						   highlightthickness=0,
						   command=lambda: self.stopIterations(),
						   relief="flat")

		self.button_stop.place(x=938.0,
							   y=802.0,
							   width=94.0,
							   height=79.0)

	def relative_to_assets(self,path: str) -> Path:
		return self.ASSETS_PATH / Path(path)

	def increaseDimCol(self):

		self.val_dim_col = int(self.val_col["text"])
		self.img_btn_inc_grid_col_pressed = tk.PhotoImage(file=self.relative_to_assets("button_inc_grid_col_pressed.png"))
		self.img_btn_inc_grid_col = tk.PhotoImage(file=self.relative_to_assets("button_inc_grid_col.png"))

		def button_press_handler(event):
			self.btn_inc_grid_col.config(image=self.img_btn_inc_grid_col_pressed)
			if self.val_dim_col < 16:
				self.val_col["text"] = f"{self.val_dim_col + 1}"
					
		self.btn_inc_grid_col.bind("<ButtonPress-1>", button_press_handler)
		return self.btn_inc_grid_col.config(image=self.img_btn_inc_grid_col)


	def decreaseDimCol(self):

		self.val_dim_col = int(self.val_col["text"])
		self.img_btn_dec_grid_col_pressed = tk.PhotoImage(file=self.relative_to_assets("button_dec_grid_col_pressed.png"))
		self.img_btn_dec_grid_col = tk.PhotoImage(file=self.relative_to_assets("button_dec_grid_col.png"))

		def button_press_handler(event):
			self.btn_dec_grid_col.config(image=self.img_btn_dec_grid_col_pressed)
			if self.val_dim_col > 1:
				self.val_col["text"] = f"{self.val_dim_col - 1}"
		
		self.btn_dec_grid_col.bind("<ButtonPress-1>", button_press_handler)
		return self.btn_dec_grid_col.config(image=self.img_btn_dec_grid_col)

	def increaseDimRow(self):

		self.val_dim_row = int(self.val_row["text"])
		self.img_btn_inc_grid_row_pressed = tk.PhotoImage(file=self.relative_to_assets("button_inc_grid_row_pressed.png"))
		self.img_btn_inc_grid_row = tk.PhotoImage(file=self.relative_to_assets("button_inc_grid_row.png"))

		def button_press_handler(event):
			self.btn_inc_grid_row.config(image=self.img_btn_inc_grid_row_pressed)
			if self.val_dim_row < 16:
				self.val_row["text"] = f"{self.val_dim_row + 1}"

		self.btn_inc_grid_row.bind("<ButtonPress-1>", button_press_handler)
		return self.btn_inc_grid_row.config(image=self.img_btn_inc_grid_row)

	def decreaseDimRow(self):

		self.val_dim_row = int(self.val_row["text"])
		self.img_btn_dec_grid_row_pressed = tk.PhotoImage(file=self.relative_to_assets("button_dec_grid_row_pressed.png"))
		self.img_btn_dec_grid_row = tk.PhotoImage(file=self.relative_to_assets("button_dec_grid_row.png"))

		def button_press_handler(event):
			self.btn_dec_grid_row.config(image=self.img_btn_dec_grid_row_pressed)
			if self.val_dim_row > 1:
				self.val_row["text"] = f"{self.val_dim_row - 1}"

		self.btn_dec_grid_row.bind("<ButtonPress-1>", button_press_handler)
		return self.btn_dec_grid_row.config(image=self.img_btn_dec_grid_row)

	def increaseCoordX(self):

		self.val_coord_x = int(self.val_x["text"])

		self.img_btn_increase_coord_x_pressed = tk.PhotoImage(file=self.relative_to_assets("button_inc_xcoord_pressed.png"))
		self.img_btn_increase_coord_x = tk.PhotoImage(file=self.relative_to_assets("button_inc_xcoord.png"))

		try:
			if self.val_coord_x < self.cols:
				self.val_x["text"] = f"{self.val_coord_x + 1}"

		except AttributeError:
			pass

		def button_press_handler(event):
			self.btn_increase_coord_x.config(image=self.img_btn_increase_coord_x_pressed)

		self.btn_increase_coord_x.bind("<ButtonPress-1>", button_press_handler)
		return self.btn_increase_coord_x.config(image=self.img_btn_increase_coord_x)

	def decreaseCoordX(self):

		self.val_coord_x = int(self.val_x["text"])

		self.img_btn_decrease_coord_x_pressed = tk.PhotoImage(file=self.relative_to_assets("button_dec_xcoord_pressed.png"))
		self.img_btn_decrease_coord_x = tk.PhotoImage(file=self.relative_to_assets("button_dec_xcoord.png"))

		try:
			if self.val_coord_x > 1:
				self.val_x["text"] = f"{self.val_coord_x - 1}"
				self.val_coord_x = int(self.val_x["text"])

		except AttributeError:
			pass

		def button_press_handler(event):
			self.btn_decrease_coord_x.config(image=self.img_btn_decrease_coord_x_pressed)

		self.btn_decrease_coord_x.bind("<ButtonPress-1>", button_press_handler)
		return self.btn_decrease_coord_x.config(image=self.img_btn_decrease_coord_x)


	def increaseCoordY(self):

		self.val_coord_y = int(self.val_y["text"])

		self.img_btn_increase_coord_y_pressed = tk.PhotoImage(file=self.relative_to_assets("button_inc_ycoord_pressed.png"))
		self.img_btn_increase_coord_y = tk.PhotoImage(file=self.relative_to_assets("button_inc_ycoord.png"))

		try:
			if self.val_coord_y < self.rows:
				self.val_y["text"] = f"{self.val_coord_y + 1}"

		except AttributeError:
			pass

		def button_press_handler(event):
			self.btn_increase_coord_y.config(image=self.img_btn_increase_coord_y_pressed)

		self.btn_increase_coord_y.bind("<ButtonPress-1>", button_press_handler)
		return self.btn_increase_coord_y.config(image=self.img_btn_increase_coord_y)

	def decreaseCoordY(self):

		self.val_coord_y = int(self.val_y["text"])
		
		self.img_btn_decrease_coord_y_pressed = tk.PhotoImage(file=self.relative_to_assets("button_dec_ycoord_pressed.png"))
		self.img_btn_decrease_coord_y = tk.PhotoImage(file=self.relative_to_assets("button_dec_ycoord.png"))

		try:
			if self.val_coord_y > 1:
				self.val_y["text"] = f"{self.val_coord_y - 1}"

		except AttributeError:
			pass

		def button_press_handler(event):
			self.btn_decrease_coord_y.config(image=self.img_btn_decrease_coord_y_pressed)

		self.btn_decrease_coord_y.bind("<ButtonPress-1>", button_press_handler)
		return self.btn_decrease_coord_y.config(image=self.img_btn_decrease_coord_y)

	def increaseGamma(self):

		self.value_gamma = float(self.val_gamma["text"])

		try:
			if self.value_gamma < 1:
				self.val_gamma["text"] = f"{(self.value_gamma + .01):.2f}"

		except AttributeError:
			pass

	def decreaseGamma(self):

		self.value_gamma = float(self.val_gamma["text"])
		
		try:
			if self.value_gamma > 0:
				self.val_gamma["text"] = f"{(self.value_gamma - .01):.2f}"

		except AttributeError:
			pass

	def increaseSteps(self):

		self.value_steps = int(self.val_steps["text"])
		
		try:
			if self.value_steps < 1000000000:
				self.val_steps["text"] = self.value_steps + 1

		except AttributeError:
			pass


	def decreaseSteps(self):

		self.value_steps = int(self.val_steps["text"])
		
		try:
			if self.value_steps > 0:
				self.val_steps["text"] = self.value_steps - 1

		except AttributeError:
			pass

 
	def increaseExplr(self):

		self.value_explr = float(self.val_explr["text"])

		try:
			if self.value_explr < 1:
				self.val_explr["text"] = f"{(self.value_explr + .01):.2f}"

		except AttributeError:
			pass

	def decreaseExplr(self):

		self.value_explr = float(self.val_explr["text"])
		
		try:
			if self.value_explr > 0:
				self.val_explr["text"] = f"{(self.value_explr - .01):.2f}"

		except AttributeError:
			pass



	def createGrid(self):

		self.img_btn_create_grid_pressed = tk.PhotoImage(file=self.relative_to_assets("create_grid_button_pressed.png"))
		self.img_btn_create_grid = tk.PhotoImage(file=self.relative_to_assets("create_grid_button.png"))

		self.destroyGrid()
		self.tile_data = np.array([])
		self.reward = 0

		self.FRM_GRID = tk.Frame(relief=tk.RAISED,
								 borderwidth=1)

		self.cols = int(self.val_col["text"])
		self.rows = int(self.val_row["text"])

		self.FRM_GRID.pack(pady=(528-25.5*self.cols,0), padx=(0,324))

		for i in range(self.cols):

			for j in range(self.rows):

				self.layout = tk.Button(master=self.FRM_GRID,
										relief=tk.RAISED,
										bg=self.tile_colors["White"],
										highlightthickness=1,
										highlightbackground="#3b4252",
										command=lambda row=i,col=j:
										self.changeTile(row,col),
										borderwidth=0)

				self.layout.grid(row=i,
								 column=j,
								 ipadx=10,
								 ipady=10)

				self.tile_data = np.append(self.tile_data, self.layout)

		self.tile_data = self.tile_data.reshape(self.cols, self.rows)

		self.val_x['text'] = '1'
		self.val_y['text'] = '1'

		def button_press_handler(event):
			self.button_create_grid.config(image=self.img_btn_create_grid_pressed)

		self.button_create_grid.bind("<ButtonPress-1>", button_press_handler)
		return self.button_create_grid.config(image=self.img_btn_create_grid)

	def initAgent(self):

		self.img_btn_place_agent_pressed = tk.PhotoImage(file=self.relative_to_assets("place_agent_button_pressed.png"))
		self.img_btn_place_agent = tk.PhotoImage(file=self.relative_to_assets("place_agent_button.png"))

		for i in range(self.cols):	
			for j in range(self.rows):
				self.tile = self.tile_data[i][j]
				self.tile["image"] = ""
		self.placeAgent()

		def button_press_handler(event):
			self.button_place_agent.config(image=self.img_btn_place_agent_pressed)

		self.button_place_agent.bind("<ButtonPress-1>", button_press_handler)
		return self.button_place_agent.config(image=self.img_btn_place_agent)

	def destroyGrid(self):

		try:
			self.FRM_GRID.destroy()
			self.layout.destroy()
			self.tile_data.destroy()

		except AttributeError:
			pass

	def changeTile(self, row, col):

		self.tile = self.tile_data[row][col]

		if self.tile["bg"] == self.tile_colors["White"]:
			self.tile["bg"] = self.tile_colors["Gray"]

		elif self.tile["bg"] == self.tile_colors["Gray"]:
			self.tile["bg"] = self.tile_colors["Blue"]

		elif self.tile["bg"] == self.tile_colors["Blue"]:
			self.tile["bg"] = self.tile_colors["Green"]

		else:
			self.tile["bg"] = self.tile_colors["White"]

		#This would be much better, if I could implement it.
		#                   ||
		#                   \/
		#self.tile["bg"] = self.tile_colors[clr % 4]

	def giveReward(self):

		if self.tile["bg"] == self.tile_colors["White"]:
			self.reward = -1

		elif self.tile["bg"] == self.tile_colors["Blue"]:
			self.reward = -10

		elif self.tile["bg"] == self.tile_colors["Green"]:
			self.reward = 10

	def placeAgent(self):

		try:
			self.xcoord = int(self.val_x["text"]) - 1
			self.ycoord = int(self.val_y["text"]) - 1
			self.tile = self.tile_data[self.xcoord][self.ycoord]
			self.tile["image"] = self.agent

		except AttributeError:
			pass

	def removeAgent(self):

		self.xcoord = int(self.val_x["text"]) - 1
		self.ycoord = int(self.val_y["text"]) - 1
		self.tile = self.tile_data[self.xcoord][self.ycoord]
		self.tile["image"] = ""

	def randomAction(self):

		self.chosen_action = self.updateUtilityGetAction()
		self.chosen_action = self.StochasticAction()

		if self.chosen_action == "LEFT":
			self.removeAgent()
			self.decreaseCoordY()
			self.placeAgent()

		elif self.chosen_action == "DOWN":
			self.removeAgent()
			self.increaseCoordX()
			self.placeAgent()

		elif self.chosen_action == "RIGHT":
			self.removeAgent()
			self.increaseCoordY()
			self.placeAgent()

		elif self.chosen_action == "UP":
			self.removeAgent()
			self.decreaseCoordX()
			self.placeAgent()


	def StochasticAction(self):

		if self.chosen_action == "LEFT":
			self.chosen_action = self.actions[random.choices(population=[3,0,1],weights=[self.xplr,1-self.optml,self.xplr],k=1)[0]]
			return self.chosen_action

		elif self.chosen_action == "DOWN":
			self.chosen_action = self.actions[random.choices(population=[0,1,2],weights=[self.xplr,1-self.optml,self.xplr],k=1)[0]]
			return self.chosen_action

		elif self.chosen_action == "RIGHT":
			self.chosen_action = self.actions[random.choices(population=[1,2,3],weights=[self.xplr,1-self.optml,self.xplr],k=1)[0]]
			return self.chosen_action

		elif self.chosen_action == "UP":
			self.chosen_action = self.actions[random.choices(population=[2,3,0],weights=[self.xplr,1-self.optml,self.xplr],k=1)[0]]
			return self.chosen_action

	def initUtilityStates(self):

		col, row = self.tile_data.shape

		for i in range(col):
			for j in range(row):
				self.tile_data[i][j]; self.tile_data[i][j].Utility = 0
	
	def updateUtilityGetAction(self):

		explr = float(self.val_explr["text"])
		self.xplr = explr/3
		self.optml = 1 - 2*self.xplr


		Utility0 = self.tile_data[int(self.xcoord)][int(self.ycoord) - 1].Utility
		Utility1 = self.tile_data[int(self.xcoord) + 1][int(self.ycoord)].Utility
		Utility2 = self.tile_data[int(self.xcoord)][int(self.ycoord) + 1].Utility
		Utility3 = self.tile_data[int(self.xcoord) - 1][int(self.ycoord)].Utility

		self.best_action = max(Utility3*self.xplr + Utility0*self.optml + Utility1*self.xplr,
							   Utility0*self.xplr + Utility1*self.optml + Utility2*self.xplr,
							   Utility1*self.xplr + Utility2*self.optml + Utility3*self.xplr,
							   Utility2*self.xplr + Utility3*self.optml + Utility0*self.xplr)																			

		self.tile_data[int(self.xcoord)][int(self.ycoord)].Utility = self.reward + float(self.val_gamma['text'])*self.best_action
		#print(self.tile_data[int(self.xcoord)][int(self.ycoord)].Utility)
		print(self.tile_data)
		b=np.zeros(self.tile_data.shape)
		for i in range(self.tile_data.shape[0]):
			for j in range(self.tile_data.shape[1]):
				b[i][j] = self.tile_data[i][j].Utility
		print(b)

		if self.best_action == Utility3*self.xplr + Utility0*self.optml + Utility1*self.xplr:
			self.chosen_action = self.actions[0]
			return self.chosen_action

		elif self.best_action == Utility0*self.xplr + Utility1*self.optml + Utility2*self.xplr:
			self.chosen_action = self.actions[1]
			return self.chosen_action

		elif self.best_action == Utility1*self.xplr + Utility2*self.optml + Utility3*self.xplr:
			self.chosen_action = self.actions[2]
			return self.chosen_action

		elif self.best_action == Utility2*self.xplr + Utility3*self.optml + Utility0*self.xplr:
			self.chosen_action = self.actions[3]
			return self.chosen_action

	def checkAction(self):

		if self.chosen_action == "LEFT" and self.tile["bg"] == self.tile_colors["Gray"]:
			self.tile_data[int(self.xcoord)][int(self.ycoord)].Utility=-2
			self.removeAgent()
			self.increaseCoordY()
			self.placeAgent()

		elif self.chosen_action == "DOWN" and self.tile["bg"] == self.tile_colors["Gray"]:
			self.tile_data[int(self.xcoord)][int(self.ycoord)].Utility=-2
			self.removeAgent()
			self.decreaseCoordX()
			self.placeAgent()

		elif self.chosen_action == "RIGHT" and self.tile["bg"] == self.tile_colors["Gray"]:
			self.tile_data[int(self.xcoord)][int(self.ycoord)].Utility=-2
			self.removeAgent()
			self.decreaseCoordY()
			self.placeAgent()

		elif self.chosen_action == "UP" and self.tile["bg"] == self.tile_colors["Gray"]:
			self.tile_data[int(self.xcoord)][int(self.ycoord)].Utility=-2
			self.removeAgent()
			self.increaseCoordX()
			self.placeAgent()

	def stopIterations(self):

		self.img_btn_stop_pressed = tk.PhotoImage(file=self.relative_to_assets("stop_button_pressed.png"))
		self.img_btn_stop = tk.PhotoImage(file=self.relative_to_assets("stop_button.png"))

		self.num_of_iter = 0

		def button_release_handler(event):
			self.button_stop.config(image=self.img_btn_stop)

		def button_press_handler(event):
			self.button_stop.config(image=self.img_btn_stop_pressed)

		self.button_stop.bind("<ButtonRelease-1>", button_release_handler)
		self.button_stop.bind("<ButtonPress-1>", button_press_handler)
		return self.button_stop.config(image=self.img_btn_stop)


	def runIterations(self): 

		self.img_btn_start_pressed = tk.PhotoImage(file=self.relative_to_assets("start_button_pressed.png"))
		self.img_btn_start = tk.PhotoImage(file=self.relative_to_assets("start_button.png"))

		self.num_of_iter = int(self.val_steps['text'])
		self.button_start.config(image=self.img_btn_start)

		try:
			self.placeAgent()
			time.sleep(0.1)
			APP.update()
			self.initUtilityStates()
			self.button_start.config(image=self.img_btn_start)

			while self.num_of_iter > 0:

				self.randomAction()
				self.checkAction()
				self.giveReward()
				self.num_of_iter -= 1
				time.sleep(0.1)
				APP.update()
				print(self.reward)

		except IndexError:
			print("In the beginning were the words, and the words made the world.")
			print("I am the words.The words are everything. Where the words end")
			print("the world ends you cannot go forward in an absence of space.")
			print("- The Talos Principle")
			num_of_iter = 0

		def button_release_handler(event):
			self.button_start.config(image=self.img_btn_start)

		def button_press_handler(event):
			self.button_start.config(image=self.img_btn_start_pressed)

		self.button_start.bind("<ButtonRelease-1>", button_release_handler)
		self.button_start.bind("<ButtonPress-1>", button_press_handler)

	def call_popup(self, APP):

		options_popup = Options(APP)
		options_popup.wait_window()

class Options(tk.Toplevel):

	def __init__(self, APP):
		tk.Toplevel.__init__(self, APP)
		self.app = APP
		self.geometry("910x1024")
		self.configure(bg="#434C5E")

		self.canvas = tk.Canvas(
		self,
		height=1024,
		width=910,
		highlightthickness=0,
		bg="#2E3440"
		)
		self.canvas.place(x=0, y=0)

		self.e1 = tk.Entry(self)
		self.e1.pack()

		self.image_1 = tk.PhotoImage(file=self.relative_to_assets("image_1.png"))
		self.canvas.create_image(686.59375, 138.1650390625, image=self.image_1)

	def relative_to_assets(self, filename):
		return os.path.join("Resources/GUI/", filename)

		def exit_popup(self):
			self.destroy()
		def relative_to_assets(self,path: str) -> Path:
			return self.ASSETS_PATH / Path(path)


APP = tk.Tk()
APP.geometry("1280x1024")
APP.title("Grid World")
APP.resizable(0,0)
GW = GridWorld(APP) 
APP.mainloop()
