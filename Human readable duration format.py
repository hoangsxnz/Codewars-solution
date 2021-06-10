def format_duration(sec):
    yrs, day, hrs, mns = 0, 0, 0, 0;
    unit, value = [], [];
    y, d, h, m, s, res =\
    " year", " day", " hour"," minute", " second", "";
    
    if sec == 0: res = "now";
        
    while sec >=  60: mns += 1; sec -=  60;       
    while mns >=  60: hrs += 1; mns -=  60;   
    while hrs >=  24: day += 1; hrs -=  24;   
    while day >= 365: yrs += 1; day -= 365;
        
    if yrs > 0:
        if yrs > 1: y += "s";
        unit.append(y); value.append(yrs);
        
    if day > 0:
        if day > 1: d += "s";
        unit.append(d); value.append(day);
        
    if hrs > 0:
        if hrs > 1: h += "s";
        unit.append(h); value.append(hrs);
        
    if mns > 0:
        if mns > 1: m += "s";
        unit.append(m); value.append(mns);
        
    if sec > 0:
        if sec > 1: s += "s";
        unit.append(s); value.append(sec);

    i = len(unit) -1;
    
    while i >= 0:
        res = str(value[i]) +unit[i] +res;        
        if i == len(unit) -1 and len(unit) > 1:
            res = ' and ' +res;
        elif i <= len(unit) -2 and i > 0:
            res = ", " +res;           
        i -= 1;
         
    return res
