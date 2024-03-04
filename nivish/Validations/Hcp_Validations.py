def check_Category(request):
    Category = request.data.get('Category')
    Category_Others = request.data.get('Category_Others')

    if Category == 'Other':
        if  Category_Others == None :
            raise Exception("Enter the text")
        
    else:
        request.data['Category_Others']= None

def check_License_Authority(request):
    License_Authority = request.data.get('License_Authority')
    License_Authority_others = request.data.get('License_Authority_others')

    if License_Authority == 'Other':
        if  License_Authority_others == None :
            raise Exception("Enter the text")
        
    else:
        request.data['License_Authority_others']= None