webpackJsonp([11], {
    1154: function (e, t, r) {
        "use strict";

        function u(e, t, r, u) {
            return (0, d.default)({
                url: p.sgkeyPrefix + "/course/queryByStudent",
                method: "post",
                data: {pageIndex: e, pageSize: t, courseType: r, liveStatusDicFk: u}
            })
        }

        function a(e, t) {
            return (0, d.default)({
                url: p.sgkeyPrefix + "/interaction/setCourseRemond",
                method: "post",
                data: {courseId: e, classId: t}
            })
        }

        function n(e, t) {
            return (0, d.default)({
                url: p.sgkeyPrefix + "/interaction/cancelCourseRemond",
                method: "post",
                data: {courseId: e, classId: t}
            })
        }

        function s(e) {
            return (0, d.default)({url: p.sgkeyPrefix + "/course/queryQqGroups", method: "post", data: {courseId: e}})
        }

        function o(e, t) {
            return (0, d.default)({
                url: p.sgkeyPrefix + "/course/queryCourseTeacher",
                method: "post",
                data: {courseId: e, classId: t}
            })
        }

        Object.defineProperty(t, "__esModule", {value: !0}), t.getCourse = u, t.setRemond = a, t.cancleRemond = n, t.queryQQGroup = s, t.queryQQ = o;
        var c = r(357), d = function (e) {
            return e && e.__esModule ? e : {default: e}
        }(c), p = r(77)
    }, 847: function (e, t, r) {
        "use strict";

        function u(e) {
            return e && e.__esModule ? e : {default: e}
        }

        Object.defineProperty(t, "__esModule", {value: !0});
        var a = r(95), n = u(a), s = r(21), o = u(s), c = r(149), d = u(c), p = r(361), l = u(p), i = r(1154),
            f = r(226), y = u(f);
        t.default = {
            namespace: "course",
            state: {
                queryCourseParam: {},
                courses: [],
                count: 0,
                vip: !1,
                public: !1,
                living: !1,
                pageSize: 10,
                pageIndex: 1,
                qqGroups: {},
                qqs: {}
            },
            subscriptions: {
                setup: function (e) {
                    var t = e.dispatch, r = e.history;
                    t({type: "handleGetCourse"}), r.listen(function (e) {
                        t({type: "updateState", payload: {path: e.pathname, query: l.default.parse(e.search)}})
                    })
                }
            },
            effects: {
                handleGetCourse: d.default.mark(function e(t, r) {
                    var u, a, n, s, o, c, p = (t.payload, r.call), l = r.put, f = r.select;
                    return d.default.wrap(function (e) {
                        for (; ;) switch (e.prev = e.next) {
                            case 0:
                                return e.next = 2, f(function (e) {
                                    return e.course
                                });
                            case 2:
                                return u = e.sent, a = u.pageSize, n = u.pageIndex, s = u.vip ? 5310 : u.public ? 5311 : void 0, o = u.living ? 6101 : void 0, e.next = 8, p(i.getCourse, n, a, s, o);
                            case 8:
                                return c = e.sent, e.next = 11, l({
                                    type: "updateState",
                                    payload: {courses: c.data.courses, count: c.data.count}
                                });
                            case 11:
                            case"end":
                                return e.stop()
                        }
                    }, e, this)
                }), handleRemond: d.default.mark(function e(t, r) {
                    var u, a = t.payload, n = void 0 === a ? {} : a, s = r.call, o = r.put;
                    return d.default.wrap(function (e) {
                        for (; ;) switch (e.prev = e.next) {
                            case 0:
                                if (u = void 0, 1 !== n.type) {
                                    e.next = 7;
                                    break
                                }
                                return e.next = 4, s(i.setRemond, n.courseId, n.classId);
                            case 4:
                                u = e.sent, e.next = 10;
                                break;
                            case 7:
                                return e.next = 9, s(i.cancleRemond, n.courseId, n.classId);
                            case 9:
                                u = e.sent;
                            case 10:
                                return e.next = 12, o({type: "updateCourseRemond", payload: n});
                            case 12:
                                y.default.msg((1 === n.type ? "\u5f00\u542f" : "\u53d6\u6d88") + "\u6210\u529f");
                            case 13:
                            case"end":
                                return e.stop()
                        }
                    }, e, this)
                }), handleQueryQQGroup: d.default.mark(function e(t, r) {
                    var u, a, s, c, p = t.payload, l = void 0 === p ? {} : p, f = r.select, y = r.call, x = r.put;
                    return d.default.wrap(function (e) {
                        for (; ;) switch (e.prev = e.next) {
                            case 0:
                                return e.next = 2, f(function (e) {
                                    return e.course
                                });
                            case 2:
                                if (u = e.sent, a = u.qqGroups, s = l.courseId, !a[s]) {
                                    e.next = 7;
                                    break
                                }
                                return e.abrupt("return");
                            case 7:
                                return e.next = 9, y(i.queryQQGroup, s);
                            case 9:
                                return c = e.sent, e.next = 12, x({
                                    type: "updateState",
                                    payload: {qqGroups: (0, o.default)({}, a, (0, n.default)({}, s, c.data.qqGroups || []))}
                                });
                            case 12:
                            case"end":
                                return e.stop()
                        }
                    }, e, this)
                }), handleQueryQQ: d.default.mark(function e(t, r) {
                    var u, a, s, c, p, l = t.payload, f = void 0 === l ? {} : l, y = r.select, x = r.call, v = r.put;
                    return d.default.wrap(function (e) {
                        for (; ;) switch (e.prev = e.next) {
                            case 0:
                                return e.next = 2, y(function (e) {
                                    return e.course
                                });
                            case 2:
                                if (u = e.sent, a = u.qqs, s = f.classId, c = f.courseId, !a[c]) {
                                    e.next = 7;
                                    break
                                }
                                return e.abrupt("return");
                            case 7:
                                return e.next = 9, x(i.queryQQ, c, s);
                            case 9:
                                return p = e.sent, e.next = 12, v({
                                    type: "updateState",
                                    payload: {qqs: (0, o.default)({}, a, (0, n.default)({}, c, p.data.teachers || []))}
                                });
                            case 12:
                            case"end":
                                return e.stop()
                        }
                    }, e, this)
                })
            },
            reducers: {
                updateState: function (e, t) {
                    var r = t.payload;
                    return (0, o.default)({}, e, r)
                }, updateCourseRemond: function (e, t) {
                    var r = t.payload, u = e.courses.map(function (e) {
                        return e.id === r.courseId ? (0, o.default)({}, e, {status: 1 === r.type ? 2010 : 2011}) : (0, o.default)({}, e)
                    });
                    return (0, o.default)({}, e, {courses: u})
                }
            }
        }, e.exports = t.default
    }
});