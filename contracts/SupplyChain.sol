// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SupplyChain {
    struct Good {
        uint256 id;
        string name;
        address manufacturer;
        address distributor;
        address retailer;
        address consumer;
        uint256 timestamp;
    }

    mapping(uint256 => Good) public goods;
    uint256 public goodsCount;

    event GoodCreated(uint256 id, string name, address manufacturer);
    event GoodTransferred(uint256 id, address from, address to);

    function createGood(string memory _name) public {
        goodsCount++;
        goods[goodsCount] = Good(goodsCount, _name, msg.sender, address(0), address(0), address(0), block.timestamp);
        emit GoodCreated(goodsCount, _name, msg.sender);
    }

    function transferGood(uint256 _id, address _to) public {
        require(goods[_id].manufacturer == msg.sender || goods[_id].distributor == msg.sender || goods[_id].retailer == msg.sender, "Unauthorized transfer");
        
        if (goods[_id].manufacturer == msg.sender) {
            goods[_id].distributor = _to;
        } else if (goods[_id].distributor == msg.sender) {
            goods[_id].retailer = _to;
        } else if (goods[_id].retailer == msg.sender) {
            goods[_id].consumer = _to;
        }
        
        emit GoodTransferred(_id, msg.sender, _to);
    }
}