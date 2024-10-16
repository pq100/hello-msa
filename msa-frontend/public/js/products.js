// 페이지 로드시 자동으로 실행
window.addEventListener('load', async () => {
    try {
         const products = await getProductList();
        // const products = null
        displayProductList(products);
    } catch (e) {
        console.log(e);
        alert('상품 목록 조회 실패!');
    }
});

// 회원 데이터 가져오기
const getProductList = async () => {
    let url = 'http://127.0.0.1:8050/products'
    const res = await fetch(url);
    if (res.ok) {
        const data = await res.json()
        return data;
    } else {
        throw new Error('상품 목록 조회 fetch 실패!!')
    }
};



// 가져온 상품 데이터 표시하기
const displayProductList = (products) => {
    // 테스트용 데이터
    // products = [{'name':'테스트', 'price':99999, 'regdate': '2024-10-16'}];

    const productlist = document.querySelector('#product-list');
    console.log(products);

    let html = '<ul>';
    for (const p of products) {
        html += `<li>
            상품 이름 : ${p.name} ,
            상품 가격 : ${p.price} ,
            상품 등록일 : ${p.regdate}
        </li>`;
    }
    html += '</ul>';

    productlist.innerHTML = html;
};