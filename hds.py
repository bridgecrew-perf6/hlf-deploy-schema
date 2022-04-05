# hlf-deploy-schema

import hashlib
import json
import os
import sys

inputFile = "./test.json"
# Input JSON file path

cmdstr = "peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C mychannel -n basic --peerAddresses localhost:7051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses localhost:9051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c \'"
# Set the command string to include peer node and certificate related paths


def parse(filename):

    with open(filename) as f:

        try:
            return json.load(f)

        except ValueError as e:
            print('invalid json: %s' % e)
            sys.exit(1)


def create():

	#print("Create Function Called")
	query = parse(inputFile)

	encoded_query = json.dumps(query).encode()

	queryHash = hashlib.sha256(encoded_query).hexdigest()
	queryString = encoded_query.decode()

	qlen = len(queryString)

	i = 0
	qs = "\\\""

	queryString = queryString.replace("\"", qs)

	cmdstr =  cmdstr + "{\"function\":\"CreateQuery\",\"Args\":[" + "\"" + queryHash + "\",\"" + queryString  + "\"]}" + "\'"


	# print(cmdstr)

	os.system(cmdstr)

def read(queryHash = None):

	#print("Read Function Called")
	#print(queryHash)

	cmdstr = "peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C mychannel -n basic --peerAddresses localhost:7051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses localhost:9051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c \'" 

	cmdstr =  cmdstr + "{\"function\":\"ReadQuery\",\"Args\":[" + "\"" + queryHash + "\"]}" + "\'"


	# print(cmdstr)

	os.system(cmdstr)


def update(queryHash = None):

	#print("Update Function Called")
	#print(queryHash)

	query = parse(inputFile)


	encoded_query = json.dumps(query).encode()



	queryHash = hashlib.sha256(encoded_query).hexdigest()
	queryString = encoded_query.decode()

	qlen = len(queryString)
	i = 0
	qs = "\\\""

	queryString = queryString.replace("\"", qs)



	cmdstr = "peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C mychannel -n basic --peerAddresses localhost:7051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses localhost:9051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c \'" 

	cmdstr =  cmdstr + "{\"function\":\"UpdateQuery\",\"Args\":[" + "\"" + queryHash + "\"]}" + "\'"


	os.system(cmdstr)

def delete(queryHash = None):

	#print("Delete Function Called")
	#print(queryHash)

	query = parse(inputFile)


	encoded_query = json.dumps(query).encode()



	queryHash = hashlib.sha256(encoded_query).hexdigest()
	queryString = encoded_query.decode()

	qlen = len(queryString)
	i = 0
	qs = "\\\""

	queryString = queryString.replace("\"", qs)



	cmdstr = "peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C mychannel -n basic --peerAddresses localhost:7051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses localhost:9051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c \'" 

	cmdstr =  cmdstr + "{\"function\":\"DeleteQuery\",\"Args\":[" + "\"" + queryHash + "\"]}" + "\'"


	os.system(cmdstr)

def main():
	if(sys.argv[1] == "create"):
		create()
	elif(sys.argv[1] == "read"):
		if(len(sys.argv) > 2):
			read(sys.argv[2])
		else:
			read()
	elif(sys.argv[1] == "update"):
		if(len(sys.argv) > 2):
			update(sys.argv[2])
		else:
			update()
	elif(sys.argv[1] == "delete"):
		if(len(sys.argv) > 2):
			delete(sys.argv[2])
		else:
			delete()
	else:
		print("Invalid Args")


if __name__ == "__main__":
	main()