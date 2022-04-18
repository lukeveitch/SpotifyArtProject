from processing_py import *
w, h = 1000, 1000

app = App(w,h) # create window: width, height
app = App(600,400) # create window: width, height
app.background(255,0,0) # set background:  red, green, blue
app.redraw() # refresh the window
app.exit() # close the window

# quads = []

# subdivisions = 50000

# # Not too small
# min_diff = 80

# # Space between quads
# sep = 1

# # Piet Mondrian Color Palette
# colors = [(38, 71, 124), (240, 217, 92), (162, 45, 40), (223, 224, 236), (223, 224, 236), (223, 224, 236), (223, 224, 236), (223, 224, 236)]

# # Subdivision adjustment
# splits = [.5, 1, 1.5]

# # Canvas Border
# edge = 10

# def random_quad():
#     return int(app.random(len(quads)))

# def setup():
#     app.size(w, h)
#     app.pixelDensity(2)
    
#     app.background(255)

#     quads = []
#     # Add the initial rectangle
#     quads.append([(edge, edge), (w - edge, edge), (w - edge, h - edge), (edge, h - edge)])
    
#     # Start splitting things up
#     for i in range(subdivisions):
#         q_index = int(app.random(len(quads)))
#         q = quads[q_index]
#         q_lx = q[0][0]
#         q_rx = q[1][0]
#         q_ty = q[0][1]
#         q_by = q[2][1]
        
#         s = splits[int(app.random(len(splits)))]
#         if (app.random(1) < .5):
#             if ((q_rx - q_lx) > min_diff):
#                 # Get new shapes x value (y is same)
#                 x_split = (q_rx - q_lx)/2 * s + q_lx
                
#                 quads.pop(q_index)
#                 quads.append([(q_lx, q_ty), (x_split - sep, q_ty), (x_split - sep, q_by), (q_lx, q_by)])
#                 quads.append([(x_split + sep, q_ty), (q_rx, q_ty), (q_rx, q_by), (x_split + sep, q_by)])
            
            
#         else:
#             if ((q_by - q_ty) > min_diff):
#                 y_split = (q_by - q_ty)/2 * s + q_ty
                
#                 quads.pop(q_index)
#                 quads.append([(q_lx, q_ty), (q_rx, q_ty), (q_rx, y_split - sep), (q_lx, y_split - sep)])
#                 quads.append([(q_lx, y_split + sep), (q_rx, y_split + sep), (q_rx, q_by), (q_lx, q_by)])
        

#     app.stroke(0)
#     app.strokeWeight(2)
#     for q in quads:
#         app.fill(*colors[int(app.random(len(colors)))])
#         app.beginShape()
#         for p in q:
#             app.vertex(p)
#         app.endShape(CLOSE)
    
#     app.save("Examples/Classic/" + str(int(app.random(10000))) + ".png")
