# Malaysia Vaccine Home Assistant Vaksin
Home Assistant - Malaysia cummulative vaccination sensor from [Our World In Data](https://ourworldindata.org/covid-vaccinations) website.

## Intro
This is the basic csv data implementation to Home Assistant via pull the data from [csv](https://github.com/owid/covid-19-data/blob/master/public/data/vaccinations/country_data/Malaysia.csv)

## How It Work
1.  Made the py code to read CSV (read the last row) and convert it to json format
2.  Extract the output json as sensor on Home Assistant configuration.yaml

## How To Setup
1.  Download [covid_vaccine_malaysia.py](covid_vaccine_malaysia.py) and put in on local folder as configuration.yaml
2.  copy code from [configuration.yaml](configuration.yaml) to our HA.

## Sensor create from configuration.yaml
1.  `vaksin_total` : total number of doses administered. This is counted as a single dose, and may not equal the total number of people vaccinated, depending on the specific dose regime (e.g. people receive multiple doses). If a person receives one dose of the vaccine, this metric goes up by 1. If they receive a second dose, it goes up by 1 again.
2.  `vaksin_vaccinated` : total number of people who received at least one vaccine dose. If a person receives the first dose of a 2-dose vaccine, this metric goes up by 1. If they receive the second dose, the metric stays the same.
3.  `vaksin_fully_vaccinated` : total number of people who received all doses prescribed by the vaccination protocol. If a person receives the first dose of a 2-dose vaccine, this metric stays the same. If they receive the second dose, the metric goes up by 1.

## Example Entities Card in Home Assistant

![vaksin_ha](/vaksin_ha.png)

## An example of how we calculate our metrics
4 people take part in a vaccination program, to be given a vaccine that requires 2 doses to be effective against the disease.

* Ali has received 2 doses;
* Abu has received 1 dose;
* Ahmad has received 1 dose;
* Ajimm has not received any dose.

In our data:

* The total number of doses administered (`vaksin_total`) will be equal to 4 (2 + 1 + 1);
* The total number of people vaccinated (`vaksin_vaccinated`) will be equal to 3 (Ali, Abu, Ahmad);
* The total number of people fully vaccinated (`vaksin_fully_vaccinated`) will be equal to 1 (Ali).

## Advance option

### Vaccination By States
Check out vaccination by states in [json](https://github.com/akutaktau/covid-19-data/blob/main/covid-19-states-vaccination-cumulatif-.json) format.

### Graph
For graphing you can get all row from this [code](covid_vaccine_malaysia_all.py)

###### FB: A Jimm Al
###### my fav local community
###### Home Assistant Malaysia https://www.facebook.com/groups/homeassistantmalaysia
###### Kelab DIY Smart Home https://www.facebook.com/groups/694589921358327
###### Telegram Group: Smart Home Malaysia https://t.me/smart_home_malaysia
