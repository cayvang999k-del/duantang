import streamlit as st
from datetime import datetime
# Chèn nhạc nền vào trang web
st.audio("Yêu Em Qua Dòng Tin Nhắn.mp3", format="audio/mp3", autoplay=True)

# ---------------------------------------------------------
# 1. CẤU HÌNH TRANG WEB
# ---------------------------------------------------------
st.set_page_config(
    page_title="Tặng Linh",
    page_icon="🍭",
    layout="centered"
)

# ---------------------------------------------------------
# 2. TẠO CÁC TAB TƯƠNG TÁC
# ---------------------------------------------------------
tab1, tab2, tab3, tab4 ,tab5 = st.tabs([
    "🏠 Trang Chủ", 
    "📸 Kỷ Niệm", 
    "💌 Tâm Tư Tui Gửi", 
    "🎮 Trò Chơi Vui" ,
    "🍭 Iu anh đi"
])

# ---------------------------------------------------------
# TAB 1: TRANG CHỦ & ĐỒNG HỒ ĐẾM NGƯỢC
# ---------------------------------------------------------
with tab1:
    st.title("💖 Chúc Mừng Ngày 20/10 Linh Nhé!")
    st.subheader("bạn gái của tôi  🍭🍭")
    
    st.markdown("---")
    
    # Tính số ngày yêu nhau (Bạn hãy chỉnh ngày bắt đầu yêu nhau ở đây: Năm, Tháng, Ngày)
    ngay_bat_dau = datetime(2026, 1, 17) # <--- SỬA NGÀY TẠI ĐÂY
    ngay_hien_tai = datetime.now()
    so_ngay_yeu = (ngay_hien_tai - ngay_bat_dau).days

    st.metric(label="🥰 Số ngày tớ và cậu đã bên nhau:", value=f"{so_ngay_yeu} ngày")
    
    st.balloons() # Hiệu ứng bóng bay khi vào trang
    st.info(" Ước mơ của anh không phải vài ba tỷ, mà 24h bên em mới là 1 ngày xa xỉ")

# ---------------------------------------------------------
# TAB 2: THƯ VIỆN KỶ NIỆM
# ---------------------------------------------------------
with tab2:
    st.header("📸 Góc seo phì ")
    st.write("Những bức ảnh đẹp ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Bức ảnh tớ thích nhất ")
        # Bạn có thể thay link ảnh bằng đường dẫn ảnh trong máy hoặc link web
        st.image("PXL_20260815_125440043~2_1.jpg", caption="iu em ")
        with st.expander("Chuyện kể đằng sau bức ảnh..."):
            st.write("Đây là một bức ảnh rất cute của linh, tớ thường khoe ảnh này với bạn bè tớ, hình ảnh đáng yêu cô gái mộc mạc thanh thoát, dễ thương vô cùng")

    with col2:
        st.subheader("Buổi hẹn hò đáng nhớ")
        st.image("1792426143199_472232705360232097_1313002359896170260_e741ec6141336f3262cee785f1ba1406.jpg", caption=" Định cắn những bông hoa nhỏ")
        with st.expander("Chuyện kể đằng sau bức ảnh..."):
            st.write("Hôm cuối ở hana, đây là lần tớ và cậu gặp lại nhau sau những biến cố, được đi bên cạnh cậu giấy phút đó thật sự là hạnh phúc, đi quanh trường như đang lướt qua xem lại những kỷ niệm mà chúng mình tạo ra, những tối chơi đàn bên em, những lần đi hẹn hò, những lần lướt qua nhau sau giờ học, nhớ lại những kỷ niệm đó, tớ thấy rất hạnh phúc khi có cậu đồng hành, tớ rất yêu em.")

# ---------------------------------------------------------
# TAB 3: HỘP THƯ MẬT MÃ
# ---------------------------------------------------------
with tab3:
    st.header(" Lời chúc 20/10 ")
    st.write("Nhập mật mã bí mật để mở thư!")
    
    mat_khaunhap = st.text_input("Nhập mật mã tại đây:", type="password")
    
    # Mật mã mặc định là 2010 (bạn có thể đổi thành ngày sinh nhật, vd: 1510)
    if mat_khaunhap == "66":
        st.success("🔓 Mở khóa thành công!")
        st.markdown("""
        ### Gửi bạn - Linh yêu dấu của tớ !
        Cảm ơn em đã luôn ở bên cạnh anh, mang lại cho anh những niềm vui và hạnh phúc. 
        Nhân ngày 20/10, Tớ chúc em luôn xinh đẹp, hạnh phúc, đạt kết quả thật cao trong học tập 
        và luôn là cô gái tuyệt vời nhất trong lòng Tôi!
        """)
        st.snow() # Hiệu ứng tuyết rơi lãng mạn
    elif mat_khaunhap != "":
        st.error("sai rồi!, gà thế,  Mật mã chưa đúng rồi, thử lại xem nào!")

# ---------------------------------------------------------
# TAB 4: TRÒ CHƠI NHỎ
# ---------------------------------------------------------
with tab4:
    st.header("Thử Thách: Đoán ý tưởng của tôi :  ")
    
    cau_hoi = st.radio(
        "Lần hẹn hò tiếp theo mình sẽ đi đâu ",
        ["Công viên", "Nhà sách", "Nhà em", "Nhà Nghỉ"]
    )
    
    if st.button("Kiểm tra câu trả lời"):
        if cau_hoi == "Nhà em":
            st.balloons()
            st.success("Chính xác 100%! bạn hiểu ý tớ thế")
        else:
            st.warning("bạn chọn sai rùi, phải là nhà em cơ !, cho anh sang nhé iu iu !!!!")
with tab5:
    st.header("Linh ơi tớ hỏi !!!")

    # Khởi tạo trạng thái lưu trữ cho Tab 5
    if "da_chon_sai_tab5" not in st.session_state:
        st.session_state.da_chon_sai_tab5 = False
    if "da_dap_dung_tab5" not in st.session_state:
        st.session_state.da_dap_dung_tab5 = False

    # Nếu chưa trả lời đúng thì hiển thị câu hỏi
    if not st.session_state.da_dap_dung_tab5:
        cau_hoi = st.radio(
            "Linh có yêu tớ không ?", 
            ["Yêu lắm", "thèm vào", "Chịu chết"],
            key="quiz_radio"
        )
        
        if st.button("Gửi câu trả lời 💌"):
            if cau_hoi == "Yêu lắm":
                st.session_state.da_dap_dung_tab5 = True
                st.session_state.da_chon_sai_tab5 = False
                st.rerun()
            else:
                st.session_state.da_chon_sai_tab5 = True
                st.rerun()

    # Nếu chọn sai -> Báo lỗi, hiện video dỗ dành/trêu và nút chọn lại
    if st.session_state.da_chon_sai_tab5 and not st.session_state.da_dap_dung_tab5: 
        # Gọi file video .mp4 có sẵn trong thư mục của bạn
        st.video("260404_230339_sh~2_1.mp4")
        
        if st.button(" cho bé chọn lại nè "):
            st.session_state.da_chon_sai_tab5 = False
            st.rerun()

    # Nếu trả lời đúng -> Bắn bong bóng mừng và hiện phần quà/lời nhắn
    if st.session_state.da_dap_dung_tab5:
        st.balloons()
        st.success("🎉 Giỏi quá! Chọn chuẩn luôn, iu bé nhất! ")
        
        # Bạn có thể chèn thêm ảnh hoặc lời nhắn ngọt ngào ở đây
        st.write("chúc bé iu có ngày 20/10 thật là hạnh phúc bên tui những phút giây này !!!!")
        
        # Cho phép chơi lại nếu muốn
        if st.button("🎮 Chơi lại thử thách"):
            st.session_state.da_dap_dung_tab5 = False
            st.session_state.da_chon_sai_tab5 = False
            st.rerun()