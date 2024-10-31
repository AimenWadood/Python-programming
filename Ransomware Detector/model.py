#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


import os

def detect_ransomware(directory):
    ransomware_extensions =  ['.locky', '.locked_file','.encrypted_file','.cryptowall', '.cryptolocker',
'.crysis',
'.arena',
'.arena',
'.aesir',
'.xort',
'.vvv',
'.ecc',
'.ezz',
'.xtbl',
'.zzz',
'.xyz',
'.zzz',
'.encrypted']  
    ransomware_detected = True

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_extension = os.path.splitext(file)[1]
            if file_extension in ransomware_extensions:
                ransomware_detected = True
                print(f"Potentially ransomware file detected: {os.path.join(root, file)}")

    if ransomware_detected:
        print("Ransomware files detected. Please take appropriate action.")
    else:
        print("All files are clean.")

if __name__ == "__main__":
    target_directory = input("Enter the directory to scan: ")
    detect_ransomware(target_directory)


# In[ ]:


import os
import time
import hashlib
import psutil

# Signature-based ransomware detection
def calculate_file_hash(file_path, hash_algorithm="sha256"):
    hash_object = hashlib.new(hash_algorithm)
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_object.update(chunk)
    return hash_object.hexdigest()

def is_ransomware_signature(file_path):
    known_ransomware_signatures = [
       "a9c4a9e47d490c2c7cb40c4cbfa35c983dbf6db4a40538a9a315381f084e69e6",  # Example signature 1
        "b5ac9e5c4db49b980539b0e3299bbf67f906d9515c06d38a12e316f0859e42b3"  # Example signature 2
        # Add known ransomware file hashes here
    ]

    file_hash = calculate_file_hash(file_path)
    return file_hash in known_ransomware_signatures

# Behavior-based ransomware detection
def monitor_directory(directory):
    while True:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_stats = os.stat(file_path)
                current_time = time.time()
                last_modified_time = file_stats.st_mtime
                time_difference = current_time - last_modified_time
                if time_difference < 10:  # Adjust this threshold as needed
                    print(f"Suspicious behavior detected in file: {file_path}")
        time.sleep(60)  # Monitor every 60 seconds

# Deception-based ransomware detection
def create_decoy_files(directory):
    decoy_file_extensions = ['.txt', '.jpg', '.pdf', '.docx']  # Add more extensions if needed

    for extension in decoy_file_extensions:
        decoy_file = os.path.join(directory, f"decoy_file{extension}")
        with open(decoy_file, "w") as f:
            f.write("This is a decoy file. Do not modify.")

def monitor_decoy_files(directory):
    while True:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if "decoy_file" in file:
                    file_path = os.path.join(root, file)
                    file_stats = os.stat(file_path)
                    current_time = time.time()
                    last_modified_time = file_stats.st_mtime
                    time_difference = current_time - last_modified_time
                    if time_difference < 10:  # Adjust this threshold as needed
                        print(f"Suspicious decoy file activity detected: {file_path}")
        time.sleep(15)  # Monitor every 60 seconds

def main():
    target_directory = input("Enter the directory to monitor: ")
    
    # Signature-based detection
    for root, dirs, files in os.walk(target_directory):
        for file in files:
            file_path = os.path.join(root, file)
            if is_ransomware_signature(file_path):
                print(f"Signature-based ransomware detected in file: {file_path}")

    # Behavior-based detection
    monitor_directory(target_directory)

    # Deception-based detection
    create_decoy_files(target_directory)
    monitor_decoy_files(target_directory)

if __name__ == "__main__":
    main()


# In[ ]:





# In[1]:


import os
import hashlib

def calculate_file_hash(file_path, hash_algorithm="sha256"):
    hash_object = hashlib.new(hash_algorithm)
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_object.update(chunk)
    return hash_object.hexdigest()

def is_ransomware_signature(file_path):
    # Define known ransomware signatures (hashes)
    known_ransomware_signatures = [
        "a9c4a9e47d490c2c7cb40c4cbfa35c983dbf6db4a40538a9a315381f084e69e6",  # Example signature 1
        "b5ac9e5c4db49b980539b0e3299bbf67f906d9515c06d38a12e316f0859e42b3",  # Example signature 2
        # Add more known ransomware signatures here
    ]

    file_hash = calculate_file_hash(file_path)
    return file_hash in known_ransomware_signatures

def main(directory):
    ransomware_detected = False

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if is_ransomware_signature(file_path):
                print(f"Ransomware signature detected in file: {file_path}")
                ransomware_detected = True

    if ransomware_detected:
        print("Signature-based ransomware detected. Please take appropriate action.")
    else:
        print("No signature-based ransomware detected.")

if __name__ == "__main__":
    target_directory = input("Enter the directory to scan: ")
    main(target_directory)


# In[2]:


import os
import time
import psutil

def monitor_directory(directory):
    while True:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                # Check if file has been modified recently
                file_stats = os.stat(file_path)
                current_time = time.time()
                last_modified_time = file_stats.st_mtime
                time_difference = current_time - last_modified_time
                if time_difference < 10:  # Adjust this threshold as needed
                    print(f"Suspicious behavior detected in file: {file_path}")
        time.sleep(10)  # Monitor every 60 seconds

def main():
    target_directory = input("Enter the directory to monitor: ")
    monitor_directory(target_directory)

if __name__ == "__main__":
    main()


# In[ ]:


pip install psutil


# In[3]:


import os
import time

def monitor_directory(directory, max_iterations=100):
    iteration = 0
    while iteration < max_iterations:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_stats = os.stat(file_path)
                current_time = time.time()
                last_modified_time = file_stats.st_mtime
                time_difference = current_time - last_modified_time
                if time_difference < 10:
                    print(f"Suspicious behavior detected in file: {file_path}")
        time.sleep(10)
        iteration += 1

def main():
    target_directory = input("Enter the directory to monitor: ")
    monitor_directory(target_directory)

if __name__ == "__main__":
    main()


# In[21]:


import os
import time

def detect_ransomware(directory, threshold=40):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_stats = os.stat(file_path)
            current_time = time.time()
            last_modified_time = file_stats.st_mtime
            time_difference = current_time - last_modified_time
            
            if time_difference < threshold:
                print(f"Potential ransomware detected: {file_path}")
                
            else:
                print("file is cleaned")

def main():
    target_directory = input("Enter the directory to scan: ")
    detect_ransomware(target_directory)

if __name__ == "__main__":
    main()
 


# In[15]:


import os
import time

def detect_ransomware(directory, threshold=10):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_stats = os.stat(file_path)
            current_time = time.time()
            last_modified_time = file_stats.st_mtime
            time_difference = current_time - last_modified_time
            
            print(f"File: {file_path}")
            print(f"Last Modified Time: {last_modified_time}")
            print(f"Current Time: {current_time}")
            print(f"Time Difference: {time_difference}")
            
            if time_difference < threshold:
                print(f"Potential ransomware detected: {file_path}")
            else:
                print(f"File is cleaned: {file_path}")

def main():
    target_directory = input("Enter the directory to scan: ")
    detect_ransomware(target_directory)

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[41]:


import os
import hashlib
import time

def calculate_file_hash(file_path, hash_algorithm="sha256"):
    hash_object = hashlib.new(hash_algorithm)
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_object.update(chunk)
    return hash_object.hexdigest()

def is_ransomware_signature(file_path):
    known_ransomware_signatures = [
        "a9c4a9e47d490c2c7cb40c4cbfa35c983dbf6db4a40538a9a315381f084e69e6",  # Example signature 1
        "b5ac9e5c4db49b980539b0e3299bbf67f906d9515c06d38a12e316f0859e42b3",  # Example signature 2
        # Add more known ransomware signatures here
    ]

    file_hash = calculate_file_hash(file_path)
    return file_hash in known_ransomware_signatures

def detect_ransomware_by_extensions(directory):
    ransomware_extensions = ['.locky', '.locked_file', '.encrypted_file', '.cryptowall', '.cryptolocker',
                            '.crysis', '.arena', '.arena', '.aesir', '.xort', '.vvv', '.ecc', '.ezz', '.xtbl',
                            '.zzz', '.xyz', '.zzz', '.encrypted']
    total_files = 0
    detected_files = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            total_files += 1
            file_extension = os.path.splitext(file)[1]
            if file_extension in ransomware_extensions:
                detected_files += 1
                print(f"Potential ransomware file detected by extension: {os.path.join(root, file)}")
            else:
                print(f"No Potential ransomware file detected by extension: {os.path.join(root, file)}")

    print(f"Total Files: {total_files}")
    print(f"Detected Files with Ransomware by Extension: {detected_files}")

def detect_ransomware_by_behavior(directory, threshold=60):
    
    detected_files = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            
            file_path = os.path.join(root, file)
            file_stats = os.stat(file_path)
            current_time = time.time()
            last_modified_time = file_stats.st_mtime
            time_difference = current_time - last_modified_time
            

            if time_difference < threshold:
                detected_files += 1
                print(f"Potential ransomware detected by behavior: {file_path}")
                print(f"Last Modified Time: {last_modified_time}")
            else:
                print(f"No Potential ransomware detected by behavior: {file_path}")

    
    print(f"Detected Files with Ransomware by Behavior: {detected_files}")

def detect_ransomware_by_signature(directory):
   
    detected_files = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            
            file_path = os.path.join(root, file)
            if is_ransomware_signature(file_path):
                detected_files += 1
                print(f"Ransomware signature detected in file: {file_path}")
            else:
                 print(f"No Ransomware signature detected in file: {file_path}")

    
    print(f"Detected Files with Ransomware by Signature: {detected_files}")

def main():
    target_directory = input("Enter the directory to scan: ")
    detect_ransomware_by_extensions(target_directory)
    detect_ransomware_by_behavior(target_directory)
    detect_ransomware_by_signature(target_directory)

if __name__ == "__main__":
    main()


# In[42]:


pip install matplotlib


# In[1]:


import os
import hashlib
import time
import matplotlib.pyplot as plt

def calculate_file_hash(file_path, hash_algorithm="sha256"):
    hash_object = hashlib.new(hash_algorithm)
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_object.update(chunk)
    return hash_object.hexdigest()

def is_ransomware_signature(file_path):
    known_ransomware_signatures = [
        "a9c4a9e47d490c2c7cb40c4cbfa35c983dbf6db4a40538a9a315381f084e69e6",  # Example signature 1
        "b5ac9e5c4db49b980539b0e3299bbf67f906d9515c06d38a12e316f0859e42b3",  # Example signature 2
        # Add more known ransomware signatures here
    ]

    file_hash = calculate_file_hash(file_path)
    return file_hash in known_ransomware_signatures

def detect_ransomware_by_extensions(directory):
    ransomware_extensions = ['.locky', '.locked_file', '.encrypted_file', '.cryptowall', '.cryptolocker',
                            '.crysis', '.arena', '.arena', '.aesir', '.xort', '.vvv', '.ecc', '.ezz', '.xtbl',
                            '.zzz', '.xyz', '.zzz', '.encrypted']
    total_files = 0
    detected_files = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            total_files += 1
            file_extension = os.path.splitext(file)[1]
            if file_extension in ransomware_extensions:
                detected_files += 1
                print(f"Potential ransomware file detected by extension: {os.path.join(root, file)}")
            else:
                print(f"No Potential ransomware file detected by extension: {os.path.join(root, file)}")

    print(f"Total Files: {total_files}")
    print(f"Detected Files with Ransomware by Extension: {detected_files}")
    return detected_files

def detect_ransomware_by_behavior(directory, threshold=60):
    
    detected_files = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            
            file_path = os.path.join(root, file)
            file_stats = os.stat(file_path)
            current_time = time.time()
            last_modified_time = file_stats.st_mtime
            time_difference = current_time - last_modified_time
            

            if time_difference < threshold:
                detected_files += 1
                print(f"Potential ransomware detected by behavior: {file_path}")
                print(f"Last Modified Time: {last_modified_time}")
            else:
                print(f"No Potential ransomware detected by behavior: {file_path}")

    
    print(f"Detected Files with Ransomware by Behavior: {detected_files}")
    return detected_files

def detect_ransomware_by_signature(directory):
   
    detected_files = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            
            file_path = os.path.join(root, file)
            if is_ransomware_signature(file_path):
                detected_files += 1
                print(f"Ransomware signature detected in file: {file_path}")
            else:
                 print(f"No Ransomware signature detected in file: {file_path}")

    
    print(f"Detected Files with Ransomware by Signature: {detected_files}")
    return detected_files

    
    
def main():
    target_directory = input("Enter the directory to scan: ")
    detected_by_extension, detected_by_behavior, detected_by_signature = 0, 0, 0

    detected_by_extension = detect_ransomware_by_extensions(target_directory)
    detected_by_behavior = detect_ransomware_by_behavior(target_directory)
    detected_by_signature = detect_ransomware_by_signature(target_directory)

   

if __name__ == "__main__":
    main()




# In[49]:


pip install Flask


# In[ ]:




