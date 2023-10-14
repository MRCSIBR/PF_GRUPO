-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS HouseMarketPrediction;

-- Use the database
USE HouseMarketPrediction;

-- Create the Region table
CREATE TABLE Region (
    RegionID INT PRIMARY KEY AUTO_INCREMENT,
    RegionName VARCHAR(255)
    -- Add other region-specific attributes here
);
-- Create the ZillowData table

CREATE TABLE ZillowData (
    ZillowID INT PRIMARY KEY,
    Zestimate DECIMAL(10, 2),
    LastUpdated DATE,
    PropertyTax DECIMAL(10, 2),
    HOAFees DECIMAL(10, 2),
    ZillowURL VARCHAR(255)
    -- Add other Zillow-specific attributes here
);

-- Create the RedfinData table
CREATE TABLE RedfinData (
    RedfinID INT PRIMARY KEY,
    RedfinEstimate DECIMAL(10, 2),
    LastUpdated DATE,
    RedfinURL VARCHAR(255)
    -- Add other Redfin-specific attributes here
);
-- Create the Property table
CREATE TABLE Property (
    PropertyID INT PRIMARY KEY AUTO_INCREMENT,
    RegionID INT,
    Address VARCHAR(255),
    City VARCHAR(255),
    State VARCHAR(255),
    ZIPCode VARCHAR(10),
    Latitude DECIMAL(10, 6),
    Longitude DECIMAL(10, 6),
    YearBuilt INT,
    PropertyType VARCHAR(255),
    Bedrooms INT,
    Bathrooms INT,
    SquareFeet INT,
    LotSize DECIMAL(10, 2),
    ZillowID INT,
    RedfinID INT,
    -- Add other property-specific attributes here
    FOREIGN KEY (RegionID) REFERENCES Region(RegionID),
    FOREIGN KEY (ZillowID) REFERENCES ZillowData(ZillowID),
    FOREIGN KEY (RedfinID) REFERENCES RedfinData(RedfinID)
);



-- Create the AirbnbData table
CREATE TABLE AirbnbData (
    AirbnbID INT PRIMARY KEY AUTO_INCREMENT,
    PropertyID INT,
    Availability VARCHAR(255),
    PricePerNight DECIMAL(10, 2),
    LastUpdated DATE,
    -- Add other Airbnb-specific attributes here
    FOREIGN KEY (PropertyID) REFERENCES Property(PropertyID)
);

-- Create the FREDData table
CREATE TABLE FREDData (
    PropertyID INT,
    InflationRate DECIMAL(5, 2),
    GDP DECIMAL(10, 2),
    UnemploymentRate DECIMAL(5, 2),
    AdditionalFREDData VARCHAR(255),
    -- Add other FRED-specific attributes here
    FOREIGN KEY (PropertyID) REFERENCES Property(PropertyID)
);

-- Create the SalesData table
CREATE TABLE SalesData (
    SaleID INT PRIMARY KEY AUTO_INCREMENT,
    PropertyID INT,
    SaleDate DATE,
    SalePrice DECIMAL(10, 2),
    BuyerName VARCHAR(255),
    -- Add other sale-related attributes herePRIMARYPRIMARY
    FOREIGN KEY (PropertyID) REFERENCES Property(PropertyID)
);

-- Create the RentalData table
CREATE TABLE RentalData (
    RentalID INT PRIMARY KEY AUTO_INCREMENT,
    PropertyID INT,
    RentalDate DATE,
    RentalPrice DECIMAL(10, 2),
    TenantName VARCHAR(255),
    -- Add other rental-related attributes here
    FOREIGN KEY (PropertyID) REFERENCES Property(PropertyID)
);
