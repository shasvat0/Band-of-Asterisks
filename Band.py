import time, sys
indent = 0
indent_increasing = True
try:
  while True:
    print(" " * indent, end="")
    print("!@#$%^&()_+~?><:!@#$%^&()+~?><:!@#$%^&*()+?><:!@#$%^&()_+~?><:!@#$%^&()_+?><")
    time.sleep(0.0001)
  
    if indent_increasing:
      indent += 1
      if indent == 20:
        indent_increasing = False
    
        
      
    else:
      indent -= 1
      if indent == 0:
        indent_increasing = True

except KeyboardInterrupt:
  sys.exit()  
      