# 엑셀 파일에서 데이터 읽어오기
plant_data = pd.read_csv('건조에 강한 실내식물.csv')  # 파일명에 맞게 변경 필요

def get_plant_info(query):
    # 사용자가 입력한 식물 이름으로 검색하여 정보 제공
    plant_info = plant_data[plant_data['이름'] == query]

    if not plant_info.empty:
        return plant_info.to_dict(orient='records')
    else:
        return None
        
def lambda_handler(event, context):
    # 사용자로부터 받은 쿼리를 파싱합니다.
    body = json.loads(event['body'])
    query = body['query']

    # 쿼리에 일치하는 식물 정보를 검색합니다.
    plants = get_plant_info(query)

    # 결과 반환
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',  # CORS 설정
        },
        'body': json.dumps({"plants": plants if plants else []})
    }
