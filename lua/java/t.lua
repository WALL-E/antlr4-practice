
function a() 
    b()
    c()
end

function b()
    c()
end

function c() 
    b()
    return
end

function d() 
    return
end

function f() 
    a()
    f()
end

