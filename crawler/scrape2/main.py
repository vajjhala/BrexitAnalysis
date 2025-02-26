from multiprocessing import Pool
from scrape import scrape
from helper import load_data, interrupt_handler_main
import time

def main(data, resume=False):
    if type(data) == list and resume:
        data = load_data(data)
    pool=[]
    while True:
        try:
            if len(data) == 1:
                data[0]['pid'] = 0
                scrape(data[0])
            else:
                for x in data: x['pid'] = -1
                pool = Pool(processes=len(data))
                pool.map(scrape, data)
                pool.close()
                pool.join()
        except KeyboardInterrupt:
            if interrupt_handler_main(KeyboardInterrupt, pool):
                month = [x['month'] for x in data]
                data = load_data(month)
                pass
            else:
                print("KeyboardInterrupt!!")
                break
        except Exception as inst:
            interrupt_handler_main(inst, pool)
            print("Error!!")
            raise
        else:
            print("We successfully scrape {} month data!!!".format(len(data)))
            break


if __name__ == '__main__':
    dic1={}
    dic2={}
    dic3={}
    querysearch = []
    monthdic = {'03': ['04', 'March'],
                '04': ['05', 'April'],
                '05': ['06', 'May'],
                '06': ['07', 'June'],
                '07': ['08', 'July'],
                '08': ['09', 'August'],
                '09': ['10', 'September']}
    month = ''
    querysearch.append("#Brexit")
   
    dic1['querysearch'] = querysearch[0]
    dic1['since'] = '2016-' + month + '-01'
    dic1['until'] = '2016-' + month + '-11'
    dic1['topTweets'] = True
    dic1['lang'] = 'en'
    dic1['refreshCursor'] = ''
    dic1['month'] = monthdic[month][1] + '1remain'
    dic1['num'] = 0

    dic2['querysearch'] = querysearch[0]
    dic2['since'] = '2016-' + month + '-11'
    dic2['until'] = '2016-' + month + '-21'
    dic2['topTweets'] = True
    dic2['lang'] = 'en'
    dic2['refreshCursor'] = ''
    dic2['month'] = monthdic[month][1] + '2remain'
    dic2['num'] = 0

    dic3['querysearch'] = querysearch[0]
    dic3['since'] = '2016-' + month + '-21'
    dic3['until'] = '2016-' + monthdic[month][0] + '-02'
    dic3['topTweets'] = True
    dic3['lang'] = 'en'
    dic3['refreshCursor'] = ''
    dic3['month'] = monthdic[month][1] + '3remain'
    dic3['num'] = 0


    data1 = [dic1]
    data2 = [dic1, dic2, dic3]
    beginT = time.time()
    data3 = ['June3']
    main(data4)
    print("Tollay running time: {}".format(time.time() - beginT))
