""" Example LSEG Data Library Code in Console """
import lseg.data as ld

if __name__ == "__main__":
    # Initialize the LSEG Data Library with your credentials
    ld.open_session()
    print("LSEG Data Library session opened successfully.")
    data = ld.get_data("AAPL.O", fields=["BID", "ASK"])
    print("Retrieved Data for AAPL.O:")
    print(data)
    # Close the session
    ld.close_session()
    print("LSEG Data Library session closed.")