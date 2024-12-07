import random
from faker import Faker

from lib.health_identifier import generate_IHI, generate_authoredOn, generate_dva, generate_hpi_i_number, generate_hpi_o_number, generate_medicare_number, generate_securemessage_endpoint
# Set Faker to use the Australian locale for more localized data
fake = Faker('en_AU')
from lib.common_health import generate_australian_gp_name, select_gender_identity, select_ASTI
import json




def generate_referral(): 
    atsi = select_ASTI()
    practitioner_role_id = fake.random_number(digits=6, fix_len=True)
    #uuid 
    referring_organization_id = fake.uuid4()
    practioner_id = fake.uuid4()
    patient_id = fake.uuid4()
    data = {
        "resourceType": "ServiceRequest",
        "id": f"AURF-{fake.random_number(digits=3, fix_len=True)}",
        "contained": [
            {
                "resourceType": "PractitionerRole",
                "id": practitioner_role_id,
                "identifier": [
                    {
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org.au/CodeSystem/v2-0203",
                                    "code": "UPIN"
                                }
                            ],
                            "text": "Medicare Provider Number"
                        },
                        "system": "http://ns.electronichealth.net.au/id/medicare-provider-number",
                        "value": generate_medicare_number()
                    }
                ],
                "practitioner": {
                    "reference": f"#{practioner_id}",
                    "type": "Practitioner"
                },
                "organization": {
                    "reference": f"#{referring_organization_id}",
                    "type": "Organization"
                }
            },
            {
                "resourceType": "Practitioner",
                "id": practioner_id,
                "identifier": [
                    {
                        "type": {
                            "coding": [
                                {
                                    "system": "http://hl7.org.au/fhir/v2/0203",
                                    "code": "NPI",
                                    "display": "National provider identifier"
                                }
                            ],
                            "text": "HPI-I"
                        },
                        "system": "http://ns.electronichealth.net.au/id/hi/hpii/1.0",
                        "value": generate_hpi_i_number()
                    }
                ],
                "name": [
                    {
                        "use": "official",
                        "family": fake.last_name(),
                        "given": [
                            fake.first_name()
                        ]
                    }
                ]
            },
            {
                "resourceType": "Organization",
                "id": referring_organization_id,
                "meta": {
                    "profile": [
                        "http://hl7.org.au/fhir/StructureDefinition/au-organization"
                    ]
                },
                "identifier": [
                    {
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org.au/CodeSystem/v2-0203",
                                    "code": "NOI",
                                    "display": "National Organisation Identifier"
                                }
                            ],
                            "text": "HPI-O"
                        },
                        "system": "http://ns.electronichealth.net.au/id/hi/hpio/1.0",
                        "value": generate_hpi_o_number()
                    },
                    {
                        "type": {
                            "coding": [
                                {
                                    "system": "http://hl7.org.au/fhir/v2/0203",
                                    "code": "RI",
                                    "display": "Resource identifier"
                                }
                            ],
                            "text": "EDI"
                        },
                        "system": "https://au.securemessagingprovider.net/edi-endpoint",
                        "value": generate_securemessage_endpoint()
                    }
                ],
                "active": True,
                "name": generate_australian_gp_name(),
                "telecom": [
                    {
                        "system": "phone",
                        "value": fake.phone_number(),
                        "use": "work"
                    },
                    {
                        "system": "email",
                        "value": fake.email(),
                        "use": "work"
                    }
                ],
                "address": [
                    {
                        "use": "work",
                        "type": "physical",
                        "line": [
                            f"{fake.street_address()}",
                        ],
                        "city": fake.city(),
                        "state": fake.state_abbr(),
                        "postalCode": fake.postcode(),
                        "country": "AUS"
                    }
                ]
            },
            {
                "resourceType": "Patient",
                "id": patient_id,
                "meta": {
                    "profile": [
                        "http://hl7.org.au/fhir/StructureDefinition/au-patient"
                    ]
                },
                "extension": [
                    {
                        "url": "http://hl7.org.au/fhir/StructureDefinition/indigenous-status",
                        "valueCoding": {
                            "system": "https://healthterminologies.gov.au/fhir/CodeSystem/australian-indigenous-status-1",
                            "code": atsi["code"],
                            "display": atsi["display"]
                        }
                    }
                ],
                "identifier": [
                    {
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "NI",
                                    "display": "National unique individual identifier"
                                }
                            ],
                            "text": "IHI"
                        },
                        "system": "http://ns.electronichealth.net.au/id/hi/ihi/1.0",
                        "value": generate_IHI()
                    },
                    {
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "MC",
                                    "display": "Patient's Medicare Number"
                                }
                            ],
                            "text": "Medicare Number"
                        },
                        "system": "http://ns.electronichealth.net.au/id/medicare-number",
                        "value": generate_medicare_number()
                    },
                    {
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org.au/CodeSystem/v2-0203",
                                    "code": "DVAU",
                                    "display": "DVA Number"
                                }
                            ],
                            "text": "DVA Number"
                        },
                        "system": "http://ns.electronichealth.net.au/id/dva",
                        "value": generate_dva()
                    }
                ],
                "name": [
                    {
                        "use": "official",
                        "family": fake.last_name(),
                        "given": [
                            fake.first_name(),
                            fake.first_name()
                        ]
                    }
                ],
                "telecom": [
                    {
                        "system": "phone",
                        "value": fake.phone_number(),
                        "use": "work",
                        "rank": 2
                    },
                    {
                        "system": "phone",
                        "value": fake.phone_number(),
                        "use": "home",
                        "rank": 2
                    },
                    {
                        "system": "phone",
                        "value": fake.phone_number(),
                        "use": "mobile",
                        "rank": 1
                    },
                    {
                        "system": "email",
                        "value": fake.email(),
                        "use": "home",
                        "rank": 2
                    }
                ],
                "gender": select_gender_identity()['Code'],
                "birthDate": f"{fake.date_of_birth(minimum_age=18, maximum_age=65)}",
                "address": [
                    {
                        "use": "home",
                        "type": "postal",
                        "line": [
                            f"{fake.street_address()}",
                        ],
                        "city": fake.city(),
                        "state": fake.state_abbr(),
                        "postalCode": fake.postcode(),
                        "country": "AUS"
                    },
                    {
                        "use": "home",
                        "type": "physical",
                        "line": [
                            f"{fake.street_address()}",
                        ],
                        "city": fake.city(),
                        "postalCode": fake.postcode(),
                        "country": "AUS"
                    }
                ],
                "contact": [
                    {
                        "relationship": [
                            {
                                "coding": [
                                    {
                                        "system": "http://health.unknown.gov.au/snomed?ItemID=10813",
                                        "code": "27",
                                        "display": "Carer"
                                    }
                                ]
                            }
                        ],
                        "name": {
                            "use": "official",
                            "family": fake.last_name(),
                            "given": [
                                fake.first_name()
                            ]
                        },
                        "telecom": [
                            {
                                "system": "phone",
                                "value": fake.phone_number(),
                                "use": "home"
                            }
                        ]
                    }
                ],
                "generalPractitioner": [
                    {
                        "reference": f"#{practitioner_role_id}",
                        "type": "PractitionerRole"
                    }
                ],
                "managingOrganization": {
                    "reference": f'#{referring_organization_id}',
                    "type": "Organization"
                }
            }
        ],
        "identifier": [
            {
                "use": "official",
                "type": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                            "code": "PLAC",
                            "display": "Placer Identifier"
                        }
                    ],
                    "text": "Placer Identifier"
                },
                "system": "http://ns.electronichealth.net.au/id/hi/hpio/1.0",
                "value": generate_hpi_o_number()
            }
        ],
        "basedOn": [
            {
                "display": "ServiceRequest"
            }
        ],
        "status": "active",
        "intent": "order",
        "priority": "routine",
        "code": {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "dummy",
                    "display": "Referral to service"
                }
            ],
            "text": "Bootcamp - Mental Health e-Referral"
        },
        "subject": {
            "reference": f"#{patient_id}",
            "type": "Patient"
        },
        "occurrenceTiming": {
            "repeat": {
                "duration": 12,
                "durationUnit": "mo"
            }
        },
        "authoredOn": generate_authoredOn(),
        "requester": {
            "reference": f"#{practitioner_role_id}",
            "type": "PractitionerRole"
        },
        "performer": [
            {
                "type": "HealthcareService",
                "identifier": {
                    "value": "dummy"
                },
                "display": "Australian Bootcamp of Clinical Health Clinic Referral Service"
            },
            {
                "type": "Organization",
                "identifier": {
                    "value": "aubootcampref"
                },
                "display": "Australian Bootcamp of Mental Health Clinic"
            }
        ]
    }

    return data


# Run the main code block only when the script is executed directly
if __name__ == "__main__":
    # Generate a referral
    referral = generate_referral()
    print(json.dumps(referral, indent=4))
