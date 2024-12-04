import boto3
import json

# Initialize Bedrock Runtime Client
bedrock_runtime_client = boto3.client('bedrock-runtime', region_name='us-east-1')

# Define the model ID
MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"

# Define the prompt
prompt = """

Convert this data :
'3478', 'AFD TECH PART OF ACCENTURE', ', part of Accenture , spécialiste du conseil en IT et Télécommunications, a rejoint le groupe Accenture en 2022. Accenture est le leader mondial des services aux entreprises et administrations, avec une expertise de pointe dans les domaines du numérique, du cloud, et de la sécurité. C’est aussi une communauté de plus de 730 000 talents et une mission commune : réaliser la promesse technologique alliée à l’ingéniosité humaine. En 2024, , filiale d’Accenture, regroupe plus de 2000 talents répartis dans 3 pays (France, Belgique et Maroc), pour un chiffre d’affaires annuel de plus de 130M€. Dans le cadre de notre croissance, nous recrutons un(e) Ingénieur(e) Kubernetes . Le poste est basé à Paris (possibilité de télétravail selon la mission). Mettre en place et gérer des conteneurs Kubernetes pour assurer la scalabilité et la fiabilité des environnements de production Automatiser les déploiements et la gestion d\'infrastructure pour optimiser les performances et la sécurité Collaborer avec les équipes de développement pour définir et intégrer des processus CI/CD Surveiller les performances et gérer les incidents en lien avec les environnements conteneurisés Assurer une veille technologique et garantir la conformité des bonnes pratiques en gestion de conteneurs', '21/11/2024', '50k-55k €⁄an', NULL, NULL, '45k-70k €⁄an', NULL, 'Profil recherché\nVous êtes diplômé(e) d’une Ecole d’Ingénieur ou d’une formation universitaire technique (BAC+5)\n\nVous justifiez d\'une expérience significative en administration de systèmes, en gestion d\'infrastructures conteneurisées, et en outils DevOps\n\nVous maîtrisez Kubernetes et avez idéalement une certification Kubernetes (CKA, CKAD, ou CKS)\n\nVous avez une bonne connaissance des langages de scripting (ex : Bash, Python) et de l\'outil Docker', 'Offre d\'emploi', ', part of Accenture, spécialiste du conseil en IT et Télécommunications, a rejoint le groupe Accenture en 2022. Accenture est le leader mondial des services aux entreprises et administrations, avec une expertise de pointe dans les domaines du numérique, du cloud, et de la sécurité. C’est aussi une communauté de plus de 730 000 talents et une mission commune : réaliser la promesse technologique alliée à l’ingéniosité humaine.\nEn 2024, , filiale d’Accenture, regroupe plus de 2000 talents répartis dans 3 pays (France, Belgique et Maroc), pour un chiffre d’affaires annuel de plus de 130M€.\nDans le cadre de notre croissance, nous recrutons un(e) Ingénieur(e) SysOps Kubernetes.\nLe poste est basé à Paris (possibilité de télétravail selon la mission).\nMettre en place et gérer des conteneurs Kubernetes pour assurer la scalabilité et la fiabilité des environnements de production\n\nAutomatiser les déploiements et la gestion d\'infrastructure pour optimiser les performances et la sécurité\n\nCollaborer avec les équipes de développement pour définir et intégrer des processus CI/CD\n\nSurveiller les performances et gérer les incidents en lien avec les environnements conteneurisés\n\nAssurer une veille technologique et garantir la conformité des bonnes pratiques en gestion de conteneurs', 'Environnement de travail\nVotre parcours candidat optimal, en 10 jours maximum !\nUn premier échange par téléphone et par Teams (ou dans nos locaux) avec un membre de l’équipe People & Project pour parler de votre profil, du poste, et de l’entreprise\n\nUn second entretien avec un Business Manager ou un Expert technique (par Teams ou dans nos locaux)\nDe la réactivité, des échanges rythmés, une expérience candidat optimale garantie avec une proposition dans les 10 jours maximum.\nBénéficiez d’un accompagnement personnalisé dès votre 1er jour d’arrivée par nos Talent Managers et votre futur Manager (accueil au siège d’Accenture ou en agence en régions, journée d’onboarding, déjeuner offert)\n\nDéveloppez vos compétences techniques, fonctionnelles ou de management, grâce au catalogue de formations Accenture\n\nFaites évoluer votre carrière grâce à notre politique de mobilité\n\nUne team E-sports engagée sur League Of Legends en Ligue Corpo Riot X Vitality, coachée par Yellowstar 😎\n\nRémunération selon profil + prime de participation + prime vacances + tickets restaurant\nVivez des expériences hors du commun avec des événements réguliers et une ambiance familiale\nNos recrutements sont fondés sur les compétences, sans distinction d’origine, d’âge, ou de genre et tous nos postes sont ouverts aux personnes en situation de handicap.\nÀ très bientôt chez part of Accenture !', '> 1 000 salariés', 'Sysops kubernetes', 'Île-de-France', 'https://www.free-work.com/fr/tech-it/autre/job-mission/sysops-kubernetes', '83', '2024-11-26', 'yahya.banouk@expersi.com', 'https://api.free-work.com/media/cache/resolve/company_logo_medium/logo-uh7uvZUEBnpJ81Ej.jpeg', '1', 'freework'
to a Json of this attributs 
    id 
    title 
    type 
    company 
    sector 
    department
    location
    remuneration_type
    remuneration 
    min_remuneration 
    max_remuneration 
    start_date
    end_date 
    duration 
    renewable 
    seniority 
    years_experience 
    telework 
    full_remote 
    telework_days 
    description 
    tasks
    required_skills 
    desired_skills
    platform 
    creation_date
    link
    user_email
    is_selected
 Note: estimate values that doesn’t exist, and give the json without writing anything else only the json
"""

# Define the payload
payload = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 2000,
    "top_k": 500,
    "temperature": 1,
    "top_p": 0.999,
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ]
}

# Call the Bedrock API
try:
    response = bedrock_runtime_client.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(payload),
        accept="application/json",
        contentType="application/json",
    )
    
    # Parse the StreamingBody response
    response_body = response['body'].read().decode('utf-8')  # Read and decode the response
    result = json.loads(response_body)  # Parse the JSON content
    print("Generated JSON Output:")
    print(json.dumps(result, indent=2))
except Exception as e:
    print(f"Error invoking model: {e}")
