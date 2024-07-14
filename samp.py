def valtim(ts):
    try:
        spli=ts.split(":")
        if len(spli)!=3:
            raise ValueError("Invalid time/Time Format")
        hr,mins,sec=spli
         
        if not (hr.isdigit() and mins.isdigit() and sec.isdigit()):
            raise ValueError("Input should be in INT")
        hr=int(hr)
        mins=int(mins)
        sec=int(sec)
        if not (hr <= 24):
            raise ValueError("Should be 24hrs or less")
        if not (0 <= mins < 60):
            raise ValueError("Should be 0-59")
        if not (0 <= sec < 60):
            raise ValueError("Should be 0-59")

        return f"Valid Time: {hr:02}:{mins:02}:{sec:02}"
    except:
        return "Invalid format"
def valtim1():
    ts= input("Enter the time:")
    fin=valtim(ts)
    print(fin)
valtim1()













    
