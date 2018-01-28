from heapq import *
class Solution:
    def minmaxGasDist(self, stations, K):
        myheap = [(-1*(stations[i+1]-stations[i]),0,(stations[i+1]-stations[i])) for i in range(len(stations)-1)]
        heapify(myheap)
        print(sorted(myheap))
        k=0 
        while k< K:
            dist=heappop(myheap)
            num_comma =1

            while dist[2]/(dist[1]+num_comma+1) > (-1*myheap[0][0]) and k+num_comma < K:
                num_comma+=1
            heappush(myheap, (-1*dist[2]/(dist[1]+num_comma+1),dist[1]+num_comma,dist[2]))

            print("{}, {}".format(k, sorted(myheap)))
            k+=num_comma

        res=-1*heappop(myheap)[0]
        return res
        
