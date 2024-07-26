letter = '''
    Dear <|Name|>,
        You are selected!
        <|Date|>
'''

# chaning replacement 

print( letter.replace("<|Name|>" , "Ayush Aryan") .replace("<|Date|>" , "19 July, 2024") )