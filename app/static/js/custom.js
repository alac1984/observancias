function showReplyForm(val) {
    val = val.split("-").pop()
    el = document.querySelector(`[value="${val}"]`).parentElement.parentElement
    if(el.style.display === "none") {
        el.style.display = "block"
        el.scrollIntoView({
            behavior: "smooth"
        })
    } else {
        el.style.display = "none"
    }
}