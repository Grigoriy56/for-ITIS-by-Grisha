def ip(list):
    twins = set()
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i][1] == list[j][1]:
                twins = twins.add(list[i])
                twins = twins.add(list[j])
    return twins