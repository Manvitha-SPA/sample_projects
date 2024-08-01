import requests
from bs4 import BeautifulSoup
def scrape(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    }
    response = requests.get(link, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        all_text = soup.get_text(separator='\n')
        text = all_text.strip()
        lines = text.splitlines()
        restaurant = lines[0].split('|')
        r_name = restaurant[0].split(',')

        restaurant_name = r_name[0]
        restaurant_address = find_address(lines)
        contact_details = find_phone_number(lines)
        Outlet_time = outlet_time(lines)
        apc_2 = apc(lines)
        s_pet = pet_frndly(lines)
        cuisines = cuisine(lines)
        info = moreinfo(lines)
        seats = seat_type(lines)
        p_methods = payment(lines)
        table_res = reservation(lines)
        parking_info = parking(lines)

        output_1 = [restaurant_name, restaurant_address, contact_details, Outlet_time, apc_2, parking_info, s_pet, cuisines, p_methods, info, seats, table_res]
        
        output = {
            'name': restaurant_name,
            'address': restaurant_address,
            'phone_num': contact_details,
            'timings': Outlet_time,
            'apc': apc_2,
            'park': parking_info,
            'pet': s_pet,
            'cui': cuisines,
            'pay': p_methods,
            'mi': info,
            'seat':seats,
            't_reserve':table_res,
        }
        
        # Create a new instance of the Restaurant model and save it to the database
        '''restaurant = Restaurant(
            R_name=output['name'],
            R_address=output['address'],
            R_phone=output['phone_num'][:20] ,
            R_timings=output['timings'],
            R_apc=output['apc'],
            R_parking=output['park'],
            R_pet=output['pet'],
            R_cu=output['cui'],
            R_pay=output['pay'],
            R_more_info=output['mi'],
            R_seat=output['seat'],
            R_reserve=output['t_reserve']
        )
        #print(restaurant)
        restaurant.save()
        '''
        return output, output_1

    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)




def find_phone_number(lines):
    for i in range(len(lines)):
        if lines[i] == "Call":
            while (lines[i+1] != "Direction"):
                return lines[i+1]

def find_address(lines):
    for i in range(0,len(lines)):
        if lines[i] == "contributors"and lines[i]!="Copy":
            return lines[i+1]
            
def outlet_time(lines):
    for i in range(0,len(lines)):
        if 'Close' in lines[i]:
            return lines[i+1]
        elif'Open' in lines[i]:
            return lines[i+1]
        

def apc(lines):
    for i in range(0,len(lines)):
        if 'Average Cost' in lines[i]:
            return lines[i+1]


def pet_frndly(lines):
    if 'Pet Friendly' in lines:
        return "Yes"
    return "No"
        
def moreinfo(lines):
    result_list = []
    # print(lines)
    for i in range(len(lines)):
        if lines[i] == "More Info":
            while i + 1 < len(lines) and lines[i + 1] != "Similar restaurants" and lines[i+1]!="Featured In" and lines[i+1]!="OUR SPONSORS" and lines[i+1]!="Are you a food blogger?":
                result_list.append(lines[i + 1])
                i += 1
            return result_list
    return result_list 
        

def parking(lines):
    if "Valet Parking Available" in lines:
        return "Yes"
    else :
        return "NO"

def cuisine(lines):
    result_list = []
    # print(lines)
    for i in range(len(lines)):
        if lines[i] == "Cuisines":
            '''while lines[i+1] != "Popular Dishes":
                result_list.append(lines[i+1])
                i+=1
            return result_list'''
            while i + 1 < len(lines) and lines[i + 1] != "Popular Dishes" and lines[i+1]!="Average Cost" and lines[i+1]!="People Say This Place Is Known For":
                result_list.append(lines[i + 1])
                i += 1
            return result_list
    return result_list 


def payment(lines):
    result_list = []
    # print(lines)
    for i in range(len(lines)):
        if lines[i] == "Cash and Cards accepted" or lines[i] == "Digital payments accepted":
            while lines[i] != "More Info":
                result_list.append(lines[i])
                i+=1
            return result_list
        else:
            f"Payment method unknown"



def seat_type(lines):
    indoor_seating = False
    outdoor_seating = False

    for line in lines:
        if 'Indoor Seating' in line:
            indoor_seating = True
        if 'Outdoor Seating' in line:
            outdoor_seating = True

    if indoor_seating and outdoor_seating:
        return 'Indoor Seating and Outdoor Seating'
    elif indoor_seating:
        return 'Indoor Seating'
    elif outdoor_seating:
        return 'Outdoor Seating'
    else:
        return 'Seating preference not specified'
    



def reservation(lines):
    if "Book a Table" in lines:
        return "yes"
    else:
        return "No"
    
