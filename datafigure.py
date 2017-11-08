import pandas as pd
import matplotlib.pyplot as plt

file_path = '/home/shiyanlou/Code/user_study.json'
file_data = pd.read_json(file_path)
data = file_data[['user_id','minutes']].groupby('user_id').sum()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('User ID')
ax.set_ylabel('Study Time')
ax.set_title('StudyData')

ax.plot(data)
plt.show()

