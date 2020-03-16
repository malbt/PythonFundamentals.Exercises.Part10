import pickle
import os
from small_town_teller import Person, Account, Bank


def write_pickle():
    custd = self.customer
    acctd = self.account
    dap_out = open(account_data.pickle, "wb")
    pickle.dump(acctd,dap_out)
    dap_out.close()

    dcp_out = open(customer_data.pickle, "wb")
    pickle.dump(acctd,dcp_out)
    dcp_out.close()


def load_pickle():
    dcp_load = open(customer_data.pickle, "rb")
    read_file = pickle.load(dcp_load)


    dap_load = open(account_data.pickle, "rb")
    read_file = pickle.load(dap_load)


