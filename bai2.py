# Danh sách đơn hàng ban đầu
express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

# Thêm đơn mới
express_orders.append("GE104")

# Đơn hỏa tốc lên đầu danh sách
express_orders.insert(0, "GE100-FAST")

# Cập nhật mã đơn hàng
express_orders[2] = "GE102-UPDATED"

# Xóa đơn bị hủy
express_orders.remove("GE103-CANCEL")

# Lấy đơn đầu tiên để giao
current_order = express_orders.pop(0)

print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)