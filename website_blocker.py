import datetime as dt

host_post = "C:\Windows\System32\drivers\etc\hosts"
address = "127.0.0.1"
end_block = dt.datetime(2022,3,29)

# user choice to block or unblock 
choice = input("Do you want to block or unblock? ")
website_list =["www.highereduhry.ac.in"]

# code to block website 
if choice == "block":
    if dt.datetime.now()<end_block:
        # if user choice is block, then specify name of website you want to block
        # webname = input("Specify you name of Website you want to block : ")
        # website_list.append(webname)
        
        with open(host_post,"r+") as file:
                content = file.read()
                for site in website_list:
                    if site in content:
                        pass
                    else:
                        file.write(address+" "+site+"\n")
                        print("Website Blocked")

# code to block website 
elif choice == "unblock":
    fname = ""
    with open(host_post, "w") as file:
        contents = file.write(fname)
        print("Website Unblocked")
