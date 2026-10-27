from pyscript import document, display

def check_country(e):
    document.getElementById("output1").innerHTML = ""
    country = {
        "ph": "Philippines",
        "us": "United States",
        "ca": "Canada",
        "au": "Australia",
        "uk": "United Kingdom"
    }

    country_code = document.getElementById("countries").value.lower()
#add a country
    country["sm"] = "Somalia"
   
    display(country.get(country_code, "Country code not found."), target = "output1")


def show_country(e):
    document.getElementById("output1").innerHTML = ""
         
    country = {
                "ph": "Philippines",
                "us": "United States",
                "ca": "Canada",
                "au": "Australia",
                "uk": "United Kingdom"
            }

    
    country_code = document.getElementById("countries").value.lower()

    show_country= country_code in country

    display("The number of countries are", len(country), target = "output1")
    display("Is the country in the dictionary?", show_country, target= "output1")

        