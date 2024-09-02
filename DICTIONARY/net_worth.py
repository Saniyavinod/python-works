employee={"name":"hari","dept":"r@d","salary":50000,"combo_offer":1000,"extra_working_days":3}

if "extra_working_days" in employee:
    offer=employee.get("extra_working_days")*employee.get("combo_offer")
    net=employee.get("salary")+offer
    print(net)

else:
    net=employee.get("salary")
    print(net)    