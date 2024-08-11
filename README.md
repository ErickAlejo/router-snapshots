# **router-snapshots**

Save snapshots of the status of your l3 routers and switches, for future comparison in case of network failures or troubleshooting

### **Goal**  
Imagine being able to compare the status of any device over the last 6 months or even the entire year  
for instance:
<br>
`python3 main.py --select 100.x.x.1 --date “Sun Jul 8” --command “ip neighbor print” --current`
<br>
  
The execution should bring us the status of the router on the "interface/print brief" command on the indicated date and also the current status indicated with the "--current" flag.

```plaintext
100.x.x.2 - "Sun Jul 8 11:00:05am"

Columns: INTERFACE, ADDRESS, MAC-ADDRESS, IDENTITY, VERSION
#  INTERFACE                ADDRESS       MAC-ADDRESS        IDENTITY  VERSION   							      
0  ether1                                 DC:2C:6E:C8:C4:1D  TEST_A    6.49.13 (stable)                    
1  sfp28-1                                70:CD:91:1B:D7:9D  TEST_B 
2  sfp28-1                                60:8A:A8:23:B2:F1  TEST_C    7.12 (stable) Nov/09/2023 07:45:06
3  TEST_D          100.10.2.50            60:8A:A8:23:B2:F1  TEST_D    7.12 (stable) Nov/09/2023 07:45:06
4  TEST_E          100.1.0.9              48:A9:8A:20:EB:38  TEST_E    2.17 CSS610-8G-2S+ 
5  TEST_F          100.1.7.9              60:8A:A8:2A:3A:FA  TEST_F    7.12 (stable) Nov/09/2023 07:45:06
6  TEST_G          100.1.8.9              60:8A:A8:2B:8F:F4  TEST_G    2.17 CSS610-8G-2S+ 
7  TEST_H          100.1.0.9              48:A9:8A:20:EB:38  TEST_H    2.17 CSS610-8G-2S+ 
8  TEST_I          100.1.7.9              60:8A:A8:2A:3A:FA  TEST_I    7.12 (stable) Nov/09/2023 07:45:06 
9  TEST_J          100.1.8.9              60:8A:A8:2B:8F:F4  TEST_J    2.17 CSS610-8G-2S+


100.x.x.1 - "Sun Jul 20 11:00:05:am"

Columns: INTERFACE, ADDRESS, MAC-ADDRESS, IDENTITY, VERSION,
#  INTERFACE                ADDRESS       MAC-ADDRESS        IDENTITY  VERSION                                   
0  ether1                                 DC:2C:6E:C8:C4:1D  TEST_A    6.49.13 (stable)
1  sfp28-1                                70:CD:91:1B:D7:9D  TEST_B                       
2  sfp28-1                                60:8A:A8:23:B2:F1  TEST_C    7.12 (stable) Nov/09/2023 07:45:06  CRS326-24S+2Q+

```

**Note :** As you can see a few days ago that router had more devices connected to its interfaces, however in the current state we see that there are only a few devices connected, this is what we want to achieve.