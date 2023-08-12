import numpy as np
import tkinter as tk
import time 
import random

class GridWorld:

    def __init__(self, APP):

        self.TILE_COLORS = {"White": "#ffffff",
                            "Gray": "#d8dee9", 
                            "Blue": "#5e81ac", 
                            "Green": "#a3be8c"}

        self.ACTIONS = ("LEFT","DOWN","RIGHT","UP")

        self.AGENT = tk.PhotoImage(file="Resources/Sprites/Drone_Loris.png")
        self.reward = 0
        self.gama = 0.7
        self.createWorld()
        self.createUI()
        self.createGrid()

    def createWorld(self):
        
        self.FRM_CREATE_WORLD = tk.Frame(master=APP,
                                         relief=tk.RIDGE,
                                         height=1024,
                                         width=852,
                                         borderwidth=5,
                                         bg="#2e3440")
    
        self.FRM_CREATE_WORLD.pack(fill=tk.BOTH,
                                   side=tk.LEFT,
                                   expand=True,
                                   padx=(10,5),
                                   pady=10) 

    def createUI(self):

        self.FRM_CREATE_UI = tk.Frame(master=APP,
                                      relief=tk.GROOVE,
                                      height=1024,
                                      width=256,
                                      borderwidth=1)

        self.FRM_CREATE_UI.pack(fill=tk.X,
                                side=tk.LEFT,
                                expand=False,
                                padx=5,
                                pady=(20,0),
                                anchor="n")

        self.FRM_MAKE_GRID = tk.Frame(master=self.FRM_CREATE_UI)

        self.FRM_MAKE_GRID.pack(fill=tk.BOTH,
                                side=tk.TOP,
                                expand=True,
                                anchor="n")

        self.LBL_MAKE_GRID = tk.Label(master=self.FRM_MAKE_GRID,
                                      width=18,
                                      text="Size of Grid")

        self.LBL_MAKE_GRID.pack(fill=None,
                                side=tk.TOP,
                                pady=20,
                                expand=False,
                                anchor="n")

        self.BTN_DECREASE_DIM_X = tk.Button(master=self.FRM_MAKE_GRID,
                                            text="-",
                                            command=self.decreaseDimX)

        self.BTN_DECREASE_DIM_X.pack(fill=tk.X,
                                    side=tk.LEFT,
                                    expand=True,
                                    anchor="center")

        self.lbl_value_dim_x =  tk.Label(master=self.FRM_MAKE_GRID,
                                        relief=tk.SUNKEN,
                                        text="0",
                                        height=2)

        self.lbl_value_dim_x.pack(fill=tk.X,
                                  side=tk.LEFT,
                                  expand=True,
                                  anchor="nw")

        self.BTN_INCREASE_DIM_X = tk.Button(master=self.FRM_MAKE_GRID,
                                            text="+",
                                            command=self.increaseDimX)

        self.BTN_INCREASE_DIM_X.pack(fill=tk.X,
                                     side=tk.LEFT,
                                     expand=True,
                                     anchor="center")

        self.BTN_DECREASE_DIM_Y = tk.Button(master=self.FRM_MAKE_GRID,
                                            text="-",
                                            command=self.decreaseDimY)

        self.BTN_DECREASE_DIM_Y.pack(fill=tk.X,
                                     side=tk.LEFT,
                                     expand=True,
                                     anchor="center")

        self.lbl_value_dim_y =  tk.Label(master=self.FRM_MAKE_GRID,
                                         relief=tk.SUNKEN,
                                         text="0",
                                         height=2)

        self.lbl_value_dim_y.pack(fill=tk.X,
                                  side=tk.LEFT,
                                  expand=True,
                                  anchor="sw")

        self.BTN_INCREASE_DIM_Y = tk.Button(master=self.FRM_MAKE_GRID,
                                            text="+",
                                            command=self.increaseDimY)

        self.BTN_INCREASE_DIM_Y.pack(fill=tk.X,
                                     side=tk.LEFT,
                                     expand=True,
                                     anchor="center")

        self.BTN_MAKE_GRID = tk.Button(master=self.FRM_CREATE_UI,
                                       text="Create Grid",
                                       command=self.createGrid)

        self.BTN_MAKE_GRID.pack(fill=tk.BOTH,
                                side=tk.TOP,
                                pady=(20,0),
                                expand=True,
                                anchor="center")
        
        self.FRM_PLACE_AGENT = tk.Frame(master=self.FRM_CREATE_UI)

        self.FRM_PLACE_AGENT.pack(fill=tk.BOTH,
                                  side=tk.TOP,
                                  expand=True,
                                  anchor="n")

        self.LBL_PLACE_AGENT = tk.Label(master=self.FRM_PLACE_AGENT,
                                        width=18,
                                        text="Place Agent")

        self.LBL_PLACE_AGENT.pack(fill=None,
                                  side=tk.TOP,
                                  pady=20,
                                  expand=True,
                                  anchor="n")

        self.BTN_DECREASE_COORD_X = tk.Button(master=self.FRM_PLACE_AGENT,
                                              text="-",
                                              command=self.decreaseCoordX)

        self.BTN_DECREASE_COORD_X.pack(fill=tk.X,
                                       side=tk.LEFT,
                                       expand=True,
                                       anchor="center")

        self.lbl_value_coord_x = tk.Label(master=self.FRM_PLACE_AGENT,
                                          relief=tk.SUNKEN,
                                          text="0",
                                          height=2)

        self.lbl_value_coord_x.pack(fill=tk.X,
                                    side=tk.LEFT,
                                    expand=True,
                                    anchor="nw")

        self.BTN_INCREASE_COORD_X = tk.Button(master=self.FRM_PLACE_AGENT,
                                              text="+",
                                              command=self.increaseCoordX)

        self.BTN_INCREASE_COORD_X.pack(fill=tk.X,
                                       side=tk.LEFT,
                                       expand=True,
                                       anchor="center")

        self.BTN_DECREASE_COORD_Y = tk.Button(master=self.FRM_PLACE_AGENT,
                                              text="-",
                                              command=self.decreaseCoordY)

        self.BTN_DECREASE_COORD_Y.pack(fill=tk.X,
                                       side=tk.LEFT,
                                       expand=True,
                                       anchor="center")

        self.lbl_value_coord_y =  tk.Label(master=self.FRM_PLACE_AGENT,
                                           relief=tk.SUNKEN,
                                           text="0",
                                           height=2)

        self.lbl_value_coord_y.pack(fill=tk.X,
                                    side=tk.LEFT,
                                    expand=True,
                                    anchor="nw")

        self.BTN_INCREASE_COORD_Y = tk.Button(master=self.FRM_PLACE_AGENT,
                                              text="+",
                                              command=self.increaseCoordY)

        self.BTN_INCREASE_COORD_Y.pack(fill=tk.X,
                                       side=tk.LEFT,
                                       expand=True,
                                       anchor="center")

        self.LBL_NUM_ITER = tk.Label(master=self.FRM_CREATE_UI, 
                                    text="Number of Iterations",
                                    width=18)

        self.LBL_NUM_ITER.pack(fill=tk.X,
                              pady=(30,0))

        self.ent_num_iter = tk.Entry(master=self.FRM_CREATE_UI,
                                    justify="center",
                                    relief=tk.SUNKEN,
                                    width=18)

        self.ent_num_iter.pack(fill=tk.X)

        self.BTN_NUM_ITER = tk.Button(master=self.FRM_CREATE_UI,
                                     relief=tk.RAISED,
                                     width=18,
                                     text="Run Iterations",
                                     command=self.runIterations)

        self.BTN_NUM_ITER.pack(fill=tk.X)

        self.BTN_ABORT = tk.Button(master=self.FRM_CREATE_UI,
                                   relief=tk.RAISED,
                                   width=18,
                                   text="Abort")

        self.BTN_ABORT.pack(fill=tk.X)

    def increaseDimX(self):

        self.value_dim_x = int(self.lbl_value_dim_x["text"])
        
        if self.value_dim_x < 18:
            self.lbl_value_dim_x["text"] = f"{self.value_dim_x + 1}"

    def decreaseDimX(self):

        self.value_dim_x = int(self.lbl_value_dim_x["text"])

        if self.value_dim_x > 0:
            self.lbl_value_dim_x["text"] = f"{self.value_dim_x - 1}"

    def increaseDimY(self):

        self.value_dim_y = int(self.lbl_value_dim_y["text"])
        
        if self.value_dim_y < 18:
            self.lbl_value_dim_y["text"] = f"{self.value_dim_y + 1}"

    def decreaseDimY(self):

        self.value_dim_y = int(self.lbl_value_dim_y["text"])

        if self.value_dim_y > 0:
            self.lbl_value_dim_y["text"] = f"{self.value_dim_y - 1}"

    def increaseCoordX(self):

        self.value_coord_x = int(self.lbl_value_coord_x["text"])
       
        if self.value_coord_x < self.value_dim_x:
            self.lbl_value_coord_x["text"] = f"{self.value_coord_x + 1}"

    def decreaseCoordX(self):

        self.value_coord_x = int(self.lbl_value_coord_x["text"])

        if self.value_coord_x > 0:
            self.lbl_value_coord_x["text"] = f"{self.value_coord_x - 1}"

    def increaseCoordY(self):

        self.value_coord_y = int(self.lbl_value_coord_y["text"])
        
        if self.value_coord_y < self.value_dim_y:
            self.lbl_value_coord_y["text"] = f"{self.value_coord_y + 1}"

    def decreaseCoordY(self):

        self.value_coord_y = int(self.lbl_value_coord_y["text"])

        if self.value_coord_y > 0:
            self.lbl_value_coord_y["text"] = f"{self.value_coord_y - 1}"

    def createGrid(self):
        
        self.destroyGrid()
        self.tile_data = np.array([])
        self.reward = 0

        self.FRM_GRID = tk.Frame(master=self.FRM_CREATE_WORLD,
                                 relief=tk.RAISED,
                                 borderwidth=1)

        self.xdim = int(self.lbl_value_dim_x["text"])
        self.ydim = int(self.lbl_value_dim_y["text"])

        self.FRM_GRID.pack(pady=(512-25.5*self.xdim,0))

        for i in range(self.xdim):

            for j in range(self.ydim):

                self.layout = tk.Button(master=self.FRM_GRID,
                                        relief=tk.RAISED,
                                        bg=self.TILE_COLORS["White"],
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

        self.tile_data = self.tile_data.reshape(self.xdim, self.ydim)

    def destroyGrid(self):

        try: 
            self.FRM_GRID.destroy()
            self.layout.destroy()
            self.tile_data.destroy()

        except AttributeError:
            pass

    def changeTile(self, row, col):

        self.tile = self.tile_data[row][col]

        if self.tile["bg"] == self.TILE_COLORS["White"]:
            self.tile["bg"] = self.TILE_COLORS["Gray"]

        elif self.tile["bg"] == self.TILE_COLORS["Gray"]:
            self.tile["bg"] = self.TILE_COLORS["Blue"]

        elif self.tile["bg"] == self.TILE_COLORS["Blue"]:
            self.tile["bg"] = self.TILE_COLORS["Green"]

        else:
            self.tile["bg"] = self.TILE_COLORS["White"]
        
        #This would be much better, if I could implement it.
        #                   ||
        #                   \/
        #self.tile["bg"] = self.TILE_COLORS[clr % 4]
    
    def giveReward(self):

        if self.tile["bg"] == self.TILE_COLORS["White"]:
            self.reward = -1

        elif self.tile["bg"] == self.TILE_COLORS["Blue"]:
            self.reward = -10

        elif self.tile["bg"] == self.TILE_COLORS["Green"]:
            self.reward = 10

    def placeAgent(self):
        
        self.xcoord = int(self.lbl_value_coord_x["text"])
        self.ycoord = int(self.lbl_value_coord_y["text"])
        self.tile = self.tile_data[self.xcoord][self.ycoord]
        self.tile["image"] = self.AGENT

    def removeAgent(self):

        self.xcoord = int(self.lbl_value_coord_x["text"])
        self.ycoord = int(self.lbl_value_coord_y["text"])
        self.tile = self.tile_data[self.xcoord][self.ycoord]
        self.tile["image"] = ""
       
    def randomAction(self):
        
#        self.chosen_action = self.ACTIONS[random.randint(0,3)] 
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
            self.chosen_action = self.ACTIONS[random.choices(population=[3,0,1],weights=[.2,.6,.2],k=1)[0]]

        elif self.chosen_action == "DOWN":
            self.chosen_action = self.ACTIONS[random.choices(population=[0,1,2],weights=[.2,.6,.2],k=1)[0]]

        elif self.chosen_action == "RIGHT":
            self.chosen_action = self.ACTIONS[random.choices(population=[1,2,3],weights=[.2,.6,.2],k=1)[0]]

        elif self.chosen_action == "UP":
            self.chosen_action = self.ACTIONS[random.choices(population=[2,3,0],weights=[.2,.6,.2],k=1)[0]]
        
        return self.chosen_action

    def initUtilityStates(self): 
        
        for i in range(self.xdim):
            for j in range(self.ydim):
                self.tile_data[i][j]; self.tile_data[i][j].Utility = 0

    def updateUtilityGetAction(self):

        Utility0 = self.tile_data[int(self.xcoord)][int(self.ycoord) - 1].Utility 
        Utility1 = self.tile_data[int(self.xcoord) + 1][int(self.ycoord)].Utility 
        Utility2 = self.tile_data[int(self.xcoord)][int(self.ycoord) + 1].Utility 
        Utility3 = self.tile_data[int(self.xcoord) - 1][int(self.ycoord)].Utility 

        self.bestAction = max(Utility3*.1 + Utility0*.8 + Utility1*.1, 
                              Utility0*.1 + Utility1*.8 + Utility2*.1, 
                              Utility1*.1 + Utility2*.8 + Utility3*.1, 
                              Utility2*.1 + Utility3*.8 + Utility0*.1)

        self.tile_data[int(self.xcoord)][int(self.ycoord)].Utility = self.reward + self.gama*self.bestAction
        print(self.tile_data[int(self.xcoord)][int(self.ycoord)].Utility)

        if self.bestAction == Utility3*.1 + Utility0*.8 + Utility1*.1:
            self.chosen_action = self.ACTIONS[0] 
            return self.chosen_action

        elif self.bestAction == Utility0*.1 + Utility1*.8 + Utility2*.1:
            self.chosen_action = self.ACTIONS[1] 
            return self.chosen_action

        elif self.bestAction == Utility1*.1 + Utility2*.8 + Utility3*.1:
            self.chosen_action = self.ACTIONS[2] 
            return self.chosen_action

        elif self.bestAction == Utility2*.1 + Utility3*.8 + Utility0*.1:
            self.chosen_action = self.ACTIONS[3] 
            return self.chosen_action

    def checkAction(self):

        if self.chosen_action == "LEFT" and self.tile["bg"] == self.TILE_COLORS["Gray"]:
            self.removeAgent()
            self.increaseCoordY()
            self.placeAgent()

        elif self.chosen_action == "DOWN" and self.tile["bg"] == self.TILE_COLORS["Gray"]:
            self.removeAgent()
            self.decreaseCoordX()
            self.placeAgent()

        elif self.chosen_action == "RIGHT" and self.tile["bg"] == self.TILE_COLORS["Gray"]:
            self.removeAgent()
            self.decreaseCoordY()
            self.placeAgent()

        elif self.chosen_action == "UP" and self.tile["bg"] == self.TILE_COLORS["Gray"]:
            self.removeAgent()
            self.increaseCoordX()
            self.placeAgent()

    def toggle(self):

        pass

    def valueIteration(self):

        pass

    def qLearning(self): 

        pass

#    def ValueIteration(self):

        #self.val_states = np.zeros(self.xdim * self.ydim)
        #self.val_states = self.val_states.reshape(self.xdim, self.ydim)
        #self.val_states[self.xcoord,self.ycoord] = self.reward() 
#        for tile in tile_data:
#            for action in self.ACTIONS:

    def runIterations(self): # Change this to def ValueIteration, initiate expected values
                             # to all states of tiles to 0, four actions for each state
                             # for arg max function use python max() to return the optimal
                             # policy for each state, then change text of tile 
                             # corresponding to the action in each state to the optimal 
                             # action(text = unicode -> leftarrow, downarrow, uparrow, 
                             # rightarrow. Run code in while/for loop until,
                             # v(nstate)-v(state) <= epilson. Also change tkinter button
                             # state from normal to disable to prevent user from 
                             # interferring with simulation. Don't need to use 
                             # discount parameter gamma since rewards in the future is 
                             # same as the present. Also T(a,s,s')=1, because the problem
                             # is deterministic and not stochastic, so we can just 
                             # neglect this term. After the first iteration each tile
                             # will have a expected value of -1. The second iteration 
                             # expected values of tiles near the terminal state will 
                             # be assign different expect value. 1*(0 + 10).

        self.num_of_iter = int(self.ent_num_iter.get())

        try:
            # for tile in tile_space:
            #     for action in actions
             
            self.placeAgent()
            time.sleep(0.1)
            APP.update() 
            self.initUtilityStates()

            while self.num_of_iter > 0:
                
                self.randomAction()
                self.checkAction()
                self.giveReward()
#                self.reward()
#                self.ValueIteration()
                self.num_of_iter -= 1
                time.sleep(0.1)
                APP.update() 
                #print(int(self.lbl_value_coord_y["text"]),int(self.lbl_value_coord_x["text"]))
#                print(self.tile_data[int(self.xcoord)][int(self.ycoord) - 1].Utility)
                print(self.reward)
#                self.tile_data[2][1]; self.tile_data[2][1].Utility = 0.223

        except IndexError:
            print("In the beginning were the words, and the words made the world.")
            print("I am the words.The words are everything. Where the words end")
            print("the world ends you cannot go forward in an absence of space.")
            print("- The Talos Principle")
            num_of_iter = 0 

APP = tk.Tk()
APP.geometry("1280x1024")
APP.title("Grid World")
APP.resizable(0,0)
GW = GridWorld(APP) 

APP.mainloop()
