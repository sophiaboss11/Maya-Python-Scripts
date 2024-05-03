import maya.cmds as cmds

# Constants for the range of meshes
START = 4
END = 7
endAll = 10 #get value

def adjust_animation_timing(start, end):
    # Loop through each mesh in the specified range
    allframes = []
    mesh_names = []
    for i in range(start, end + 1):
        mesh_name = f"anim_mesh_{i}"
        # Get all keyframes for the mesh
        keyframes = cmds.keyframe(mesh_name, query=True)
        allframes.append(keyframes)
        mesh_names.append(mesh_name)
            
    print("get frames: " + str(allframes))
    count = 0

    for meshIndex, key_times in enumerate(allframes):
        for frameIndex, key_time in enumerate(key_times):
            
            if count%3 == 0 or count == 0:
                key_time -= 1
            elif count%3 == 2 or count == 2:
                key_time += 1

            key_time += meshIndex
            # print(mesh_names[meshIndex] + ", currentTime: " + str(allframes[meshIndex][frameIndex]))

            cmds.keyframe(mesh_names[meshIndex], edit=True, 
                time=(allframes[meshIndex][frameIndex], 
                    allframes[meshIndex][frameIndex]), timeChange=i)

                
            allframes[meshIndex][frameIndex] = key_time
            
            count+=1
        
        print("\n")       
    print("transformed frames: " + str(allframes))
    # for end - end all, shift frames


adjust_animation_timing(START, END)