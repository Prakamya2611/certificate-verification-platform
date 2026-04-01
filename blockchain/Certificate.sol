// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CertificateRegistry {

    // Store certificate hashes
    mapping(string => bool) private certificates;

    // Add a certificate hash
    function addCertificate(string memory certHash) public {
        certificates[certHash] = true;
    }

    // Verify certificate hash
    function verifyCertificate(string memory certHash) public view returns (bool) {
        return certificates[certHash];
    }
}
