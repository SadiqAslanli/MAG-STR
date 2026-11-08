text_sample = "Bakalavriat sÉ™viyyÉ™sindÉ™ ixtisasÄ±n ÅŸifri vÉ™ adÄ± Magistratura sÉ™viyyÉ™sindÉ™ uyÄŸun ixtisaslarÄ±n (ixtisaslaÅŸmalarÄ±n) ÅŸifri vÉ™ adÄ± Proq-ram â„–-si TÉ™lÉ™b olunan minimal bal **050607 Elektrik vÉ™ elektronika mÃ¼hÉ™ndisliyi"

decoded = text_sample.encode('latin1').decode('utf-8')
print("Decoded cleanly:")
print(decoded)
