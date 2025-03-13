def bioskopAlproo(jumlahTiket,jumlahPopcorn,jumlahSoda,hari):
    
    
    try:
        jumlahTicket = int(ticket)
        jumlahPopcorn = int(popcorn)
        jumlahSoda = int(soda)
        hari = int(hari)
        
        
        if jumlahTiket < 0 or  jumlahPopcorn < 0 or  jumlahSoda < 0 or  hari < 0 or jumlahTiket > 6 or  jumlahPopcorn > 6 or  jumlahSoda > 6 or  hari > 6:
            print("pilihan hari hanya 0-6") 
     
        if hari == 0 or hari == 1 or hari == 2 or hari == 3:
            ticket = 40000
            popcorn = 35000
            soda = 20000
        elif hari == 4:
            ticket = 45000
            popcorn = 30000
            soda = 15000
        else:
            ticket = 50000
            popcorn = 40000
            soda = 25000
            
        if jumlahTicket == jumlahPopcorn and jumlahTicket == jumlahSoda:
            ticket = ticket * jumlahTicket * 25/100
        elif jumlahTicket == jumlahPopcorn or jumlahTicket == jumlahSoda:
            ticket = ticket * jumlahTicket * 10/100
        elif jumlahTicket < jumlahPopcorn and jumlahTicket < jumlahSoda:
            ticket = ticket * jumlahTicket
            
        popcorn = popcorn * jumlahPopcorn
        soda = soda * jumlahSoda
        harga_akhir = ticket + popcorn + soda
        
        
        print(f"Harga Tiket : {ticket}")
        print(f"Harga Popcorn : {popcorn}") 
        print(f"Harga Soda : {soda}") 
        print(f"Harga Total : {harga_akhir}")     
    
    except ValueError as e:
         print(e)