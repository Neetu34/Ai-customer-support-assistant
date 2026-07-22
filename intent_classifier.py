def classify_intent(query):
    query = query.lower()

    if any(word in query for word in [
        "product",
        "price",
        "cost",
        "available",
        "availability",
        "laptop",
        "phone",
        "headphone"
    ]):
        return "Product Inquiry"

    elif any(word in query for word in [
        "order",
        "track",
        "tracking",
        "delivery",
        "delayed",
        "shipping"
    ]):
        return "Order Status"

    elif any(word in query for word in [
        "return",
        "refund",
        "replacement",
        "damaged"
    ]):
        return "Returns & Refunds"

    elif any(word in query for word in [
        "login",
        "password",
        "payment",
        "website",
        "error",
        "technical",
        "not working"
    ]):
        return "Technical Support"

    else:
        return "General Query"