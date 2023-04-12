text='successfully created the build stage for jenkin-rfp project demo'
with open('/var/jenkins_home/newfile.txt', 'w') as file:
    # Write the data from the original file to the new file
    file.write(text)

# Confirm that the new file has been created and written to
print("File saved successfully!")
