def final_value_after_operations(operations):
    my_dict = {"bouncy": 1, "flouncy": 1, "trouncy": -1, "pouncy": -1}

    tigger = 1
    
    
    for i in range(len(operations)):
        tigger += my_dict[operations[i]]
                    
    return tigger



operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))