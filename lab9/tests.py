def main():
	print("#testing driver car model#")
	test_driver=driver.Driver()

	print("#standard input test#")
	test_driver.moveright(3)
	assert test_driver.getcoordinates()==(3,0)

	print('#zero input test#')
	test_driver.moveright(0)
	assert test_driver.getcoordinates()==(3,0)

	print('#negative input test#')
	test_driver.moveright(-1)
	assert test_driver.getcoordinates()==(2,0)

	print("#testing traffic model#")
	test_traffic=driver.Traffic()

	print('#standard input test#')
	test_traffic.speedup(2)
	assert test_traffic.speedup()==(0,2)

	print('#zero input test#')
	test_traffic.speedup(0)
	assert test_traffic.speedup()==(0,2)

	print('#negative input test#')
	test_traffic.speedup(-1)
	assert test_traffic.speedup()==(0,1)
main()
