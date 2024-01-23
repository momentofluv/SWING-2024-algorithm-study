def solution(participant, completion):
    completion.sort()
    participant.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[len(participant)-1]

#test 1
#print(solution(	["leo", "kiki", "eden"], ["eden", "kiki"]))

#test 2
'''print(solution(["marina", "josipa", "nikola", "vinko", "filipa"]
, ["josipa", "filipa", "marina", "nikola"])) '''

#test 3
#print(solution(	["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))