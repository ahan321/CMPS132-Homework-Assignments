# Recitation 1
# Name: Ahan Malli
# Worked With: David Oke

def translate(translation:dict, msg:str):
    msg_array = msg.lower().strip(".").split()
    print(msg_array)
    keys = translation.keys()

    for i in range(len(msg_array)):
        finder = False
        for j in keys:
            if j == msg_array[i]:
                finder = True
        
        if finder == True:
            value = msg_array.pop(i)
            msg_array.insert(i,translation[value])
    return " ".join(msg_array)

myDict = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', '1':'2'}
text = '1 UP 2 down left, right forward.'
translate(myDict, text)