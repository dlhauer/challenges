def avoidFlood(rains):
    lakes = dict()
    dry_days = []

    for i, lake in enumerate(rains):
        if lake == 0:
            dry_days.append(i)
        if lake in lakes and dry_days:
            dry_day = None
            for j, day in enumerate(dry_days):
                if day > lakes[lake][-1]:
                    dry_day = (j, day)
                    break
            if dry_day is not None:
                rains[dry_days.pop(dry_day[0])] = lake
                lakes[lake].pop()
        if lake in lakes:
            lakes[lake].append(i)
            if len(lakes[lake]) > 1:
                return []
        elif lake != 0:
            lakes[lake] = [i]
        rains[i] = -1
    
    for dry_day in dry_days:
        rains[dry_day] = 1
    
    return rains

rains = [0,0,1,0,1,1]
print(avoidFlood(rains))