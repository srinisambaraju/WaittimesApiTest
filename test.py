import os

done = False
fileexists = False
while not fileexists:
    for root, dirs, files in os.walk('C:/Downloads/AttDashboard'):
        for file in files:
            if file.endswith('.zip'):
                print(os.path.join(root,file))
                done = True
                fileexists = True
                break
        if done:
            print('Hello I am in done condition')
            break

    if fileexists:
        print('Hello I am in filexists condition')
        break

