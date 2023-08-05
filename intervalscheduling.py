class Solution:
    def interval_scheduling(self, intervals):
            #type intervals: list of int tuples
            #return type: list of int tuples

            endpoint = 0
            beginpoint = 0
            append1 = []
            intervals = sorted(intervals, key=lambda x: x[1])
            print(intervals)
            for b in range(len(intervals)):
                append1.append([])
                for i in range(0,len(intervals),b+1):
                    if  intervals[i][1] > endpoint:
                        if  intervals[i][0] >= endpoint:
                            endpoint = intervals[i][1]
                            beginpoint = intervals[i][0]
                            print((beginpoint, endpoint))
                            append1[b].append((beginpoint, endpoint))
            print(beginpoint, endpoint)

            print(append1)
            greatest = 0
            best = 0
            greatestbegin = 0
            for i in append1:
                if len(i) > greatest:
                    greatest = len(i)
                    best = i
                if len(i) == greatest:
                    if i[0][0] > greatestbegin:
                        greatestbegin = i[0][0]
                        greatest = len(i)
                        best = i
            print(best)
            return best
                
                 

            
            #TODO: Write code below to return an int tuples list with the solution to the prompt.
            pass



def main():
    string = input()
    string = string.replace(" ", "")  # Remove any whitespace in the string
    string = string.replace("),", ")|")  # Replace the comma between tuples with a custom separator
    
    list_from_string = string.split("|")  # Split the string into individual tuple strings
    
    # Convert the tuple strings to actual tuples
    result = [eval(tuple_str) for tuple_str in list_from_string]

                
    tc1= Solution()
    ans=tc1.interval_scheduling(result)
    print(ans)
    
if __name__ == "__main__":
    main()
  
