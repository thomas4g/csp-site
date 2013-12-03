
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from scheduler.forms import DataEntryForm
from CspScheduler.ConstraintParser import create_schedule

# Create your views here.


def formatReturnValues(resultList):
    print "HELLO WORLD"
    if resultList is None:
        return("No schedule possible.")
    else:
        newResultList = []
        for eachClass in resultList:
            print eachClass.data['school'], " ", eachClass.data['name']
            section = resultList[eachClass]
            if section is None:
                newResultList.append(eachClass.data['school']+" "+eachClass.data['name']+" is not in the schedule")
            else:
                newResultList.append(eachClass.data['school']+" "+eachClass.data['name'])
                for meeting in section['meetings']:
                    m = 'M' if meeting['monday'] else ' '
                    t = 'T' if meeting['tuesday'] else ' '
                    w = 'W' if meeting['wednesday'] else ' '
                    r = 'R' if meeting['thursday'] else ' '
                    f = 'F' if meeting['friday'] else ' '
                    newResultList.append(m+t+w+r+f)
        return newResultList

def data_entry(request):
    if not request.user.is_authenticated():
        return HttpResponse("access denied")
    else:
        if request.method == 'POST':
            form = DataEntryForm(request.POST)
            if form.is_valid:
                classOptions = request.POST['Class_Options']
                minHours = request.POST['Minimum_Hours']
                maxHours = request.POST['Maximum_Hours']
                startTime = "2001-01-01T"+request.POST['Start_Time']+"Z"
                endTime = "2001-01-01T"+request.POST['End_Time']+"Z"
                requiredClasses = request.POST['Required_Classes']
                classList = classOptions.split("\r\n")
                minHours = int(minHours)
                maxHours = int(maxHours)
                #Times needs some work I think
                reqClassList = requiredClasses.split("\r\n")
                result = create_schedule(classList,{"max_hours":maxHours,"min_hours":minHours,"classes_needed":reqClassList,"start_time":startTime,"end_time":endTime})
                print(result)
                newResult = formatReturnValues(result)
                return StreamingHttpResponse(newResult)
        else:
            form = DataEntryForm()
        return render(request, 'scheduler/app.html', {'form': form})