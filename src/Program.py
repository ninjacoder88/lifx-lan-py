def discover():
    build_light_get_state_packet()
    #listen for results
    #store result in json file
    
    build_device_get_group_packet()
    #listen for results
    #add group details to light details
    
    build_device_get_location_packet()
    #listen for results
    #add location details to light details
    
    return
    
def ask_for_task(task_id):
    task_dictionary = {1:"turn off light", 2:"turn on light"}
    
    for k,v in task_dictionary.items():
        print(k, v)
        
    print("choose a task")
    
    return
    
discover()
ask_for_task()