from datetime import date, timedelta

def point_for_daily_login(model):
    date1 = date(2011, 10, 10)
    date2 = date1 + timedelta(days=5)
    print (date2)

def point_for_add_puzzle(Points):

    current_points = Points.for_add
    current_amt_adds =  Points.amt_adds + 1
    add_points = current_amt_adds // 10

    Points.for_add = current_points + 1 + add_points
    Points.amt_adds = current_amt_adds
    Points.save()

def point_for_add_company(Points):
    """
    It's only for adnim or superuser
    :param Points: it's model Points
    :return:
    """

    current_points = Points.for_add
    current_amt_adds =  Points.amt_adds + 1
    add_points = current_amt_adds // 100

    Points.for_add = current_points + 5 + add_points
    Points.amt_adds = current_amt_adds
    Points.save()

def point_for_comment(Points):

    # current amt comments + new
    current_amt_comments = Points.amt_comments + 1

    add_points = current_amt_comments // 20
    Points.for_comments += 5 + add_points
    Points.amt_comments = current_amt_comments
    Points.save()

def point_for_edit(Points):

    current_amt_edits = Points.amt_edits + 1
    add_points = current_amt_edits // 10

    Points.for_edit += 2 + add_points
    Points.amt_edits = current_amt_edits
    Points.save()

def point_for_visit(Points):

    current_amt_visits = Points.amt_visits + 1
    add_points = current_amt_visits // 10

    Points.for_visit += 2 + add_points
    Points.amt_visits = current_amt_visits
    Points.save()



