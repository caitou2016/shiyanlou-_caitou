import pandas as pd

def analysis(file,user_id):
    times = 0
    minutes = 0
    file_path = '/home/shiyanlou/Code/{}.json'.format(file)
    try:
        data = pd.read_json(file_path)
    except:
        return times,minutes

    times = data[data['user_id']==user_id]['minutes'].count()
    minutes = data[data['user_id']==user_id]['minutes'].sum()
    return times,minutes

if __name__ == '__main__':
    file = 'user_study'
    user_id = 184704
    print(analysis(file,user_id))
